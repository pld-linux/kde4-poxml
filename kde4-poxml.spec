#
# TODO:
# - add man files
#
%define		orgname		poxml
%define		_state		stable
%define		qtver		4.8.1

Summary:	An xml2po and vice versa converters
Summary(pl.UTF-8):	Konwertery po2xml i vice versa
Name:		kde4-%{orgname}
Version:	4.14.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	7e3f458fa794d3687884283f8a97593e
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	antlr
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	hunspell-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	/usr/bin/python
Obsoletes:	kde4-kdesdk-po2xml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An xml2po and vice versa converters.

%description -l pl.UTF-8
Konwertery po2xml i vice versa.

%description
poxml.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/po2xml
%attr(755,root,root) %{_bindir}/split2po
%attr(755,root,root) %{_bindir}/swappo
%attr(755,root,root) %{_bindir}/xml2pot
%{_mandir}/man1/*
