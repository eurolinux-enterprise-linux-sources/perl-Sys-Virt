Name:           perl-Sys-Virt
Version:        2.0.0
Release:        1%{?dist}
Summary:        Represent and manage a libvirt hypervisor connection
License:        GPLv2+ or Artistic
URL:            http://search.cpan.org/dist/Sys-Virt/
Source0:        http://www.cpan.org/authors/id/D/DA/DANBERR/Sys-Virt-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libvirt-devel >= %{version}
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::XPath::XMLParser)
# Optional tests only
BuildRequires:  perl(Test::CPAN::Changes)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
The Sys::Virt module provides a Perl XS binding to the libvirt virtual
machine management APIs. This allows machines running within arbitrary
virtualization containers to be managed with a consistent API.

%prep
%setup -q -n Sys-Virt-%{version}
sed -i -e '/Sys-Virt\.spec/d' Makefile.PL
sed -i -e '/\.spec\.PL$/d' MANIFEST
rm -f *.spec.PL

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc AUTHORS Changes README examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%changelog
* Fri Jul  1 2016 Daniel P. Berrange <berrange@redhat.com> - 2.0.0-1
- Rebase to 2.0.0 release (rhbz #1286682)

* Mon Apr 18 2016 Daniel P. Berrange <berrange@redhat.com> - 1.3.3-1
- Rebase to 1.3.3 release (rhbz #1286682)

* Wed Mar  9 2016 Daniel P. Berrange <berrange@redhat.com> - 1.3.2-1
- Rebase to 1.3.2 release (rhbz #1286682)

* Fri Jul 17 2015 Daniel P. Berrange <berrange@redhat.com> - 1.2.17-2
- Avoid coverity strncpy() warning

* Fri Jul 17 2015 Daniel P. Berrange <berrange@redhat.com> - 1.2.17-1
- Rebase to 1.2.17 release (rhbz #1194602)

* Wed May  6 2015 Daniel P. Berrange <berrange@redhat.com> - 1.2.15-1
- Rebase to 1.2.15 release (rhbz #1194602)

* Wed Dec 17 2014 Daniel P. Berrange <berrange@redhat.com> - 1.2.8-6
- Add VIR_CONNECT_GET_ALL_DOMAINS_STATS_BACKING constant (rhbz #1175314)

* Thu Dec 11 2014 Daniel P. Berrange <berrange@redhat.com> - 1.2.8-5
- Fix crash with migrate_to_uri API (rhbz #1171938)

* Thu Dec  4 2014 Daniel P. Berrange <berrange@redhat.com> - 1.2.8-4
- Add agent lifecycle event callbacks & constants (rhbz #1167392)
- Fix docs for get_time method (rhbz #1164972)
- Fix docs for GET_ALL_STATS constnats (rhbz #1170481)

* Mon Nov 10 2014 Daniel P. Berrange <berrange@redhat.com> - 1.2.8-3
- Update for latest constants in libvirt (rhbz #1160793)

* Tue Sep 30 2014 Daniel P. Berrange <berrange@redhat.com> - 1.2.8-2
- Update for latest constants/events in libvirt (rhbz #1147042)

* Wed Sep 10 2014 Daniel P. Berrange <berrange@redhat.com> - 1.2.8-1
- Update to 1.2.8 release (rhbz #1140194)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.1.1-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.1-4
- Mass rebuild 2013-12-27

* Wed Dec 18 2013 Daniel P. Berrange <berrange@redhat.com> - 1.1.1-3
- Fix out of bounds read in migrate param handling (rhbz #1043736)

* Thu Aug  8 2013 Daniel P. Berrange <berrange@redhat.com> - 1.1.1-2
- Fix incorrect handling of flags in $dom->get_vcpu_info() (rhbz #994139)
- Fix error handling in $dev->get_parent() (rhbz #994141)

* Tue Jul 30 2013 Daniel P. Berrange <berrange@redhat.com> - 1.1.1-1
- Update to 1.1.1 release

* Tue Jul 30 2013 Daniel P. Berrange <berrange@redhat.com> - 1.1.0-1
- Update to 1.1.0 release

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.0.5-2
- Perl 5.18 rebuild

* Tue May 14 2013 Daniel P. Berrange <berrange@redhat.com> - 1.0.5-1
- Update to 1.0.5 release

* Tue Mar  5 2013 Daniel P. Berrange <berrange@redhat.com> - 1.0.3-1
- Update to 1.0.3 release

* Wed Feb 27 2013 Daniel P. Berrange <berrange@redhat.com> - 1.0.2-1
- Update to 1.0.2 release

* Tue Feb 26 2013 Daniel P. Berrange <berrange@redhat.com> - 1.0.1-1
- Update to 1.0.1 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Daniel P. Berrange <berrange@redhat.com> - 1.0.0-1
- Update to 1.0.0 release

* Wed Sep 26 2012 Daniel P. Berrange <berrange@redhat.com> - 0.10.2-1
- Update to 0.10.2 release

* Mon Sep 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.10.0-1
- Update to 0.10.0 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 0.9.13-2
- Perl 5.16 rebuild

* Mon Jul  2 2012 Daniel P. Berrange <berrange@redhat.com> - 0.9.13-1
- Update to 0.9.13 release

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.9.12-2
- Perl 5.16 rebuild

* Mon May 21 2012 Daniel P. Berrange <berrange@redhat.com> - 0.9.12-1
- Update to 0.9.12 release

* Mon Apr 16 2012 Daniel P. Berrange <berrange@redhat.com> - 0.9.11-1
- Update to 0.9.11 release

* Mon Feb 13 2012 Daniel P. Berrange <berrange@redhat.com> - 0.9.10-1
- Update to 0.9.10 release

* Mon Jan  9 2012 Daniel P. Berrange <berrange@redhat.com> - 0.9.9-1
- Update to 0.9.9 release

* Tue Jan  3 2012 Daniel P. Berrange <berrange@redhat.com> - 0.9.8-1
- Update to 0.9.8 release

* Tue Nov  8 2011 Daniel P. Berrange <berrange@redhat.com> - 0.9.7-1
- Update to 0.9.7 release

* Mon Oct 17 2011 Daniel P. Berrange <berrange@redhat.com> - 0.9.5-2
- Add binding for virDomainOpenConsole

* Thu Sep 29 2011 Daniel P. Berrange <berrange@redhat.com> - 0.9.5-1
- Update to 0.9.5 release

* Wed Aug  3 2011 Daniel P. Berrange <berrange@redhat.com> - 0.9.4-2
- Re-add virDomainAbortJob API binding accidentally removed

* Wed Aug  3 2011 Daniel P. Berrange <berrange@redhat.com> - 0.9.4-1
- Update to 0.9.4 release

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.9.3-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.9.3-2
- Perl mass rebuild

* Tue Jul 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.9.3-1
- Update to 0.9.3 release

* Fri Jul  8 2011 Daniel P. Berrange <berrange@redhat.com> - 0.9.2-1
- Update to 0.9.2 release

* Wed Jun 29 2011 Daniel P. Berrange <berrange@redhat.com> - 0.2.7-1
- Update to 0.2.7 release

* Thu May 19 2011 Matthew Booth <mbooth@redhat.com> - 0.2.6-3
- Backport get_xml_description with flags

* Wed Feb 16 2011 Daniel P Berrange <berrange@berrange.com> - 0.2.6-2
- Workaround Test::More's inability to cast XML::XPath::Number to an int

* Wed Feb 16 2011 Daniel P Berrange <dan@berrange.com> - 0.2.6-1
- Update to 0.2.6 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2.4-3
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Aug 14 2010 Daniel P. Berrange <berrange@redhat.com> - 0.2.4-2
- Rebuild against perl 5.12.0
- Fix hostname test

* Wed May 19 2010 Daniel P. Berrange <berrange@redhat.com> - 0.2.4-1
- Update to 0.2.4 release

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2.3-2
- Mass rebuild with perl-5.12.0

* Fri Jan 15 2010 Daniel P. Berrange <berrange@redhat.com> - 0.2.3-1
- Update to 0.2.3 release

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.2.1-2
- rebuild against perl 5.10.1

* Wed Aug 26 2009 Stepan Kasal <skasal@redhat.com> - 0.2.1-1
- new upstream version
- remove upstreamed patch

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Stepan Kasal <skasal@redhat.com> - 0.2.0-2
- BR: libvirt >= 0.6.1

* Mon Mar 30 2009 Stepan Kasal <skasal@redhat.com> - 0.2.0-1
- new upstream version (#237421)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Mar 07 2008 Daniel P. Berrange <berrange@redhat.com> - 0.1.2-3
- Fix calls to free() in XS binding

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.2-2
Rebuild for new perl

* Wed Mar 05 2008 Steven Pritchard <steve@kspei.com> 0.1.2-1
- Update to 0.1.2.
- Drop Sys-Virt-doc.patch.
- BR XML::XPath.
- No longer need to BR pkgconfig or xen-devel.
- Disable 100-connect test.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.1-10
- Autorebuild for GCC 4.3

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.1.1-9
- BR ExtUtils::MakeMaker.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.1.1-8
- Use fixperms macro instead of our own chmod incantation.

* Mon Aug 28 2006 Steven Pritchard <steve@kspei.com> 0.1.1-7
- Rebuild.

* Sat Aug 19 2006 Steven Pritchard <steve@kspei.com> 0.1.1-6
- More documentation fixes.

* Fri Aug 18 2006 Steven Pritchard <steve@kspei.com> 0.1.1-5
- Make this spec work on FC5 or FC6.
- Add ExclusiveArch to match xen and libvirt.

* Fri Aug 18 2006 Steven Pritchard <steve@kspei.com> 0.1.1-4
- BR xen-devel.

* Fri Aug 18 2006 Steven Pritchard <steve@kspei.com> 0.1.1-3
- BR Test::Pod and Test::Pod::Coverage.

* Sat Aug 12 2006 Steven Pritchard <steve@kspei.com> 0.1.1-2
- Add Sys-Virt-Domain-doc.patch.

* Sat Aug 12 2006 Steven Pritchard <steve@kspei.com> 0.1.1-1
- Specfile autogenerated by cpanspec 1.68.
- BR libvirt-devel and pkgconfig.
- Fix License.
- Drop non-doc autobuild.sh and add the examples directory.
- Don't try to build the included perl-Sys-Virt.spec.
