%global srcname ansible_role_redhat_subscription
%global rolename ansible-role-redhat-subscription

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Ansible role for setting up Red Hat Subscription Management.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-redhat-subscription
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python2-pbr

Requires: ansible

%description

Ansible role to configure Red Hat Subscription Management

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%py2_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py2_install


%files
%doc README*
%license LICENSE
%{python2_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Mon Feb 26 2018 RDO <dev@lists.rdoproject.org> 1.0.1-1
- Update to 1.0.1


