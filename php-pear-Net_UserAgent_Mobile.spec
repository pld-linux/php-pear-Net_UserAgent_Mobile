%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	UserAgent
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Mobile

Summary:	%{_pearname} - HTTP mobile user agent string parser
Summary(pl.UTF-8):	%{_pearname} - analizator identyfikatora przenośnych przeglądarek HTTP
Name:		php-pear-%{_pearname}
Version:	0.30.0
Release:	3
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b47d7ce95ee02aab2d07dae7baa49757
URL:		http://pear.php.net/package/Net_UserAgent_Mobile/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_UserAgent_Mobile parses HTTP_USER_AGENT strings of (mainly
Japanese) mobile HTTP user agents. It'll be useful in page dispatching
by user agents. This package was ported from Perl's HTTP::MobileAgent.
See http://search.cpan.org/search?mode=module&query=HTTP-MobileAgent.
The author of the HTTP::MobileAgent module is Tatsuhiko Miyagawa.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_UserAgent_Mobile analizuje łańcuchy HTTP_USER_AGENT (głównie
japońskich) przenośnych przeglądarek HTTP. Moduł ten może być
przydatny przy wysyłaniu stron w zależności od przeglądarki. Został
przeportowany z perlowego HTTP::MobileAgent - więcej informacji pod
http://search.cpan.org/search?mode=module&query=HTTP-MobileAgent.
Autorem modułu HTTP::MobileAgent jest Tatsuhiko Miyagawa.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Mobile
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Mobile/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
