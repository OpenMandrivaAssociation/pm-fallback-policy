Summary:	Power management fallback policy
Name:		pm-fallback-policy
Version:	0.1
Release:	12
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://wiki.mandriva.com/Docs/Hardware/PowerManagement
Source0:	power-event
Source1:	sleep-event
Source2:	pm-fallback-shutdown
Source3:	pm-fallback-suspend
BuildArch:	noarch
Conflicts:	suspend-scripts < 1.27

%description
This package provides a set of scripts to implement a power management
fallback policy. They will be used as fallback when no power
management tool is running.

%prep
%setup -q -c -T

%build

%install
install -d %{buildroot}%{_sysconfdir}/acpi/events
install %{SOURCE0} %{buildroot}%{_sysconfdir}/acpi/events/power
install %{SOURCE1} %{buildroot}%{_sysconfdir}/acpi/events/sleep
install -d %{buildroot}%{_sysconfdir}/acpi/actions
install -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/acpi/actions/pm-fallback-shutdown
install -m 755 %{SOURCE3} %{buildroot}%{_sysconfdir}/acpi/actions/pm-fallback-suspend

%post
[ -x /etc/init.d/acpid ] && service acpid condrestart || :

%files
%{_sysconfdir}/acpi/actions/*
%{_sysconfdir}/acpi/events/*

