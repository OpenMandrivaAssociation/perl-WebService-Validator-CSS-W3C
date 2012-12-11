%define upstream_name    WebService-Validator-CSS-W3C
%define upstream_version 0.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Interface to the W3C CSS Validator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(SOAP::Lite)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::QueryParam)
BuildArch:	noarch

%description
This module is an interface to the W3C CSS Validation online service the
http://jigsaw.w3.org/css-validator/ manpage, based on its SOAP 1.2 support.
It helps to find errors in Cascading Style Sheets.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 658455
- rebuild for updates rpm-setup

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 381316
- removing unused buildrequires:
- adding missing buildrequires:
- import perl-WebService-Validator-CSS-W3C


* Sat May 30 2009 cpan2dist 0.2-1mdv
- initial mdv release, generated with cpan2dist

