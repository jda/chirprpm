Name:           chirp
Version:        0.1.12
Release:        6%{?dist}
Summary:        A tool for programming two-way radio equipment

Group:          Applications/Communications
License:        GPLv3+
URL:            http://chirp.danplanet.com/
Source0:        http://chirp.danplanet.com/download/0.1.12/%{name}-%{version}.tar.gz
# Installing correct .desktop file
# Source:http://dp67.fedorapeople.org/pkgs/DESKTOP/chirp.desktop
Source1:        %{name}.desktop
# COPYING file likes to live in a peculiar place. Moving it to the proper docs directory.
# Patch Source: http://dp67.fedorapeople.org/pkgs/PATCHES/chirp-COPYING-setup.py.patch
Patch0:         chirp-COPYING-setup.py.patch
# #!/usr/bin/python shebang in every file adds noise to rpmlint.. fixing
# Patch Source: http://dp67.fedorapeople.org/pkgs/PATCHES/chirp-0.1.12-shebang.patch
Patch1:         chirp-0.1.12-shebang.patch

# BuildRoot tag left in for potential EPEL Packaging.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  desktop-file-utils
Requires:       pyserial

%description
Chirp is a tool for programming two-way radio equipment
It provides a generic user interface to the programming
data and process that can drive many radio models under
the hood.

%prep
%setup -q
%patch0 -p1 -b chirp-COPYING-setup.py.patch
%patch1 -p1 -b chirp-0.1.12-shebang.patch

%build
%{__python} setup.py build

%install
# rm -rf $RPM_BUILD_ROOT tag left in for potential EPEL Packaging.
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

# Wrong .desktop config lets install the correct .desktop
desktop-file-install \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

# Clean section left in for potential EPEL Packaging.
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/chirpw
%{python_sitelib}/%{name}-%{version}-py2.7.egg-info
# Doesn't own this directory, let's own it.
%dir %{python_sitelib}/%{name}/
# Put files in directory.
%{python_sitelib}/%{name}/*
# Doesn't own this directory, let's own it.
%dir %{python_sitelib}/chirpui/
# Put files in directory.
%{python_sitelib}/chirpui/*
%{_datadir}/applications/%{name}.desktop
# Doesn't own this directory, let's own it.
%dir %{_datadir}/%{name}/
# Put files in directory.
%{_datadir}/%{name}/*.xsd
%{_mandir}/man1/chirpw.1.gz
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-5
- Add source for .desktop, per review

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-4
- Add source for patches, per review

* Sun Nov 20 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-3
- Submit for review

* Sat Nov 19 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-2
- Own unowned directories
- Add correct .desktop file
- Apply patch to move COPYING file to proper directory
- Add shebang patch removes shebang from unnecessary files

* Sat Nov 19 2011 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 0.1.12-1
- Initial Build and testing
