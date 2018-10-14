#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Expand
Version  : 0.04
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/String-Expand-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/String-Expand-0.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-expand-perl/libstring-expand-perl_0.04-3.debian.tar.xz
Summary  : |-
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-String-Expand-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
NAME
"String::Expand" - string utility functions for expanding variables in
self-referential sets

%package dev
Summary: dev components for the perl-String-Expand package.
Group: Development
Provides: perl-String-Expand-devel = %{version}-%{release}

%description dev
dev components for the perl-String-Expand package.


%package license
Summary: license components for the perl-String-Expand package.
Group: Default

%description license
license components for the perl-String-Expand package.


%prep
%setup -q -n String-Expand-0.04
cd ..
%setup -q -T -D -n String-Expand-0.04 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/String-Expand-0.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Expand
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-String-Expand/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-String-Expand/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/String/Expand.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Expand.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Expand/LICENSE
/usr/share/package-licenses/perl-String-Expand/deblicense_copyright
