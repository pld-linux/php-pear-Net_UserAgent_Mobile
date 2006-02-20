%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	UserAgent
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Mobile

Summary:	%{_pearname} - HTTP mobile user agent string parser
Summary(pl):	%{_pearname} - analizator identyfikatora przeno¶nych przegl±darek HTTP
Name:		php-pear-%{_pearname}
Version:	0.25.0
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7f26ec24dbd083355fd554f701de1189
URL:		http://pear.php.net/package/Net_UserAgent_Mobile/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_UserAgent_Mobile parses HTTP_USER_AGENT strings of (mainly
Japanese) mobile HTTP user agents. It'll be useful in page dispatching
by user agents. This package was ported from Perl's HTTP::MobileAgent.
See http://search.cpan.org/search?mode=module&query=HTTP-MobileAgent.
The author of the HTTP::MobileAgent module is Tatsuhiko Miyagawa.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_UserAgent_Mobile analizuje ³añcuchy HTTP_USER_AGENT (g³ównie
japoñskich) przeno¶nych przegl±darek HTTP. Modu³ ten mo¿e byæ
przydatny przy wysy³aniu stron w zale¿no¶ci od przegl±darki. Zosta³
przeportowany z perlowego HTTP::MobileAgent - wiêcej informacji pod
http://search.cpan.org/search?mode=module&query=HTTP-MobileAgent.
Autorem modu³u HTTP::MobileAgent jest Tatsuhiko Miyagawa.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
