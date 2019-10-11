Summary: NFS-Ganesha 3.0 packages from the CentOS Storage SIG repository
Name: centos-release-nfs-ganesha30
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-NFS-Ganesha-30.repo
BuildArch: noarch

%if 0%{?centos} >= 7
# $contentdir for altarch support was added with CentOS-7.5
Requires: centos-release >= 7-5.1804.el7.centos.2
%endif
# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

Provides: centos-release-nfs-ganesha = 30

%description
yum configuration for NFS-Ganesha 3.0 packages from the CentOS Storage SIG.
NFS-Ganesha 3.0 will receive updates for approximately 12 months. For more
details about the release and maintenance schedule, see
https://github.com/nfs-ganesha/nfs-ganesha/wiki

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-NFS-Ganesha-30.repo
%if 0%{?centos} < 7
sed -i 's/i\$contentdir/centos/g' %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-NFS-Ganesha-30.repo
%endif

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-NFS-Ganesha-30.repo

%changelog
* Fri Oct 11 2019 Kaleb S KEITHLEY <kkeithle at redhat.com> - 1.0-1
- NFS-Ganesha 3.0
