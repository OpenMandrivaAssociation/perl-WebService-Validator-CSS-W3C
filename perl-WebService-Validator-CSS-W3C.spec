%define upstream_name    WebService-Validator-CSS-W3C
%define upstream_version 0.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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


