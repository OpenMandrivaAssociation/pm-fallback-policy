%define name pm-fallback-policy
%define version 0.1
%define release %mkrel 11

Summary: Power management fallback policy
Name: %{name}
Version: %{version}
Release: %{release}
Source0: power-event
Source1: sleep-event
Source2: pm-fallback-shutdown
Source3: pm-fallback-suspend
License: GPL
Group: System/Kernel and hardware
Url: http://wiki.mandriva.com/Docs/Hardware/PowerManagement
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Conflicts: suspend-scripts < 1.27

%description
This package provides a set of scripts to implement a power management
fallback policy. They will be used as fallback when no power
management tool is running.

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_sysconfdir}/acpi/events
install %{SOURCE0} %{buildroot}%{_sysconfdir}/acpi/events/power
install %{SOURCE1} %{buildroot}%{_sysconfdir}/acpi/events/sleep
install -d %{buildroot}%{_sysconfdir}/acpi/actions
install -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/acpi/actions/pm-fallback-shutdown
install -m 755 %{SOURCE3} %{buildroot}%{_sysconfdir}/acpi/actions/pm-fallback-suspend

%clean
rm -rf %{buildroot}

%post
[ -x /etc/init.d/acpid ] && service acpid condrestart || :

%files
%defattr(-,root,root)
%{_sysconfdir}/acpi/actions/*
%{_sysconfdir}/acpi/events/*




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-9mdv2011.0
+ Revision: 667788
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2011.0
+ Revision: 607183
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2010.1
+ Revision: 523689
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-6mdv2010.0
+ Revision: 426731
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.1-5mdv2009.1
+ Revision: 351650
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 225018
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.1-3mdv2008.1
+ Revision: 125460
- kill re-definition of %%buildroot on Pixel's request


* Fri Mar 23 2007 Olivier Blin <oblin@mandriva.com> 0.1-3mdv2007.1
+ Revision: 148264
- conflicts will old suspend-scripts

* Fri Mar 23 2007 Olivier Blin <oblin@mandriva.com> 0.1-3mdv2007.1
+ Revision: 148237
- do not conflict with suspend-scripts to ease upgrade, pm-utils will take care of the proper package ordering

* Tue Feb 27 2007 Olivier Blin <oblin@mandriva.com> 0.1-2mdv
+ Revision: 126220
- check for acpid service presence before trying to restart it

* Thu Jan 11 2007 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2007.1
+ Revision: 107584
- initial pm-fallback-policy release
- Create pm-fallback-policy

