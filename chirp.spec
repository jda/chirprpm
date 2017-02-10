%global src_name chirp-daily

Name:           chirp
Version:        20170115
Release:        2%{?dist}
Summary:        A tool for programming two-way radio equipment

Group:          Applications/Communications
License:        GPLv3+
URL:            http://chirp.danplanet.com/
Source0:        http://trac.chirp.danplanet.com/chirp_daily/daily-%{version}/%{src_name}-%{version}.tar.gz
# Installing correct .desktop file
# Source:http://dp67.fedorapeople.org/pkgs/DESKTOP/chirp.desktop
Source1:        %{name}.desktop

Patch0:         chirp-0.2.2-install.patch

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-python
BuildRequires:  pyserial

Requires:       libxml2-python
Requires:       pyserial
Requires:       python-suds


%description
Chirp is a tool for programming two-way radio equipment
It provides a generic user interface to the programming
data and process that can drive many radio models under
the hood.


%prep
%setup -q -n %{src_name}-%{version}
%patch0 -p1 -b .inst


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

# Wrong .desktop config lets install the correct .desktop
desktop-file-install \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%find_lang CHIRP


%files -f CHIRP.lang
%license COPYING
%{_bindir}/chirpw
%{python_sitelib}/%{src_name}_%{version}-py2.7.egg-info
%{python_sitelib}/%{name}/
%{_datadir}/applications/%{name}.desktop
%exclude %{_datadir}/%{name}/locale
%{_datadir}/%{name}/
%{_mandir}/man1/chirpw.1.gz
%{_datadir}/pixmaps/%{name}.png


%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Richard Shaw <hobbes1069@gmail.com> - 20170115-1
- Update to latest upstream release.

* Tue Oct 18 2016 Richard Shaw <hobbes1069@gmail.com> - 20161018-1
- Update to latest upstream release.

* Tue Aug 23 2016 Richard Shaw <hobbes1069@gmail.com> - 20160819-1
- Update to latest upstream release.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20160706-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul  7 2016 Richard Shaw <hobbes1069@gmail.com> - 20160706-1
- Update to latest upstream release.

* Mon May 23 2016 Richard Shaw <hobbes1069@gmail.com> - 20160517-1
- Update to latest upstream release.

* Wed May  4 2016 Richard Shaw <hobbes1069@gmail.com> - 20160504-1
- Update to latest upstream release.

* Wed Apr  6 2016 Richard Shaw <hobbes1069@gmail.com> - 20160402-1
- Update to latest upstream release.

* Wed Mar  9 2016 Richard Shaw <hobbes1069@gmail.com> - 20160309-1
- Update to latest upstream release.

* Mon Feb 29 2016 Richard Shaw <hobbes1069@gmail.com> - 20160229-1
- Update to latest upstream release.

* Thu Feb 18 2016 Richard Shaw <hobbes1069@gmail.com> - 20160215-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Richard Shaw <hobbes1069@gmail.com> - 20151130-1
- Update to new rolling release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct  9 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4.1-1
- Update to latest bugfix release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Richard Shaw <hobbes1069@gmail.com> - 0.4.0-1
- Update to latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.1-1
- Update to latest upstream release.

* Sat Feb 16 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.0-1
- Update to latest upstream release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.2-1
- Update to latest upstream release.

* Sun Mar 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.0-1
- Update to latest upstream release.

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
