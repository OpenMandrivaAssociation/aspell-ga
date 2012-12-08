%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 4.5-0
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Irish
%define languagecode ga
%define lc_ctype ga_IE

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	4.5.0
Release:	%mkrel 1
Group:		System/Internationalization
Source:		http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPLv2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires:	aspell >= %{aspell_ver}
BuildRequires:	make
Requires:	aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}

Obsoletes:	ispell-%{languagecode}, iirish, ispell-gaeilge

Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr %{buildroot}

%makeinstall_std

cp doc/README README.%{languagecode}
chmod 644 README* Copyright doc/*

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright 
%{_libdir}/aspell-%{aspell_ver}/*



%changelog
* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 4.5.0-1mdv2012.0
+ Revision: 701870
- New version: 4.5.0

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 4.4.0-4
+ Revision: 662815
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 4.4.0-3mdv2011.0
+ Revision: 603210
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 4.4.0-2mdv2010.1
+ Revision: 518924
- rebuild

* Sat Jun 27 2009 Isabel Vallejo <isabel@mandriva.org> 4.4.0-1mdv2010.0
+ Revision: 390010
- update to 4.4

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 3.6.0-6mdv2009.1
+ Revision: 350026
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 3.6.0-5mdv2009.0
+ Revision: 220379
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 3.6.0-4mdv2008.1
+ Revision: 182440
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 3.6.0-2mdv2007.0
+ Revision: 123257
- Import aspell-ga

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 3.6.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Wed Feb 16 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 3.6.0-1mdk
- new release

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 3.5.0-1mdk
- new release

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.4-1mdk
- updated to 0.50.4

