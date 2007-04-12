%define name pm-fallback-policy
%define version 0.1
%define release %mkrel 3

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


