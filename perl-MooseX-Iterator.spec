%define upstream_name    MooseX-Iterator
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Iterate over collections
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is an attempt to add smalltalk-like streams to Moose. It currently
works with ArrayRefs and HashRefs.

* next

  The next method provides the next item in the colletion.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 656943
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 607004
- import perl-MooseX-Iterator

