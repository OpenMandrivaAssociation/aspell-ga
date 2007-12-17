%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 3.6-0
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Irish
%define languagecode ga
%define lc_ctype ga_IE

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       3.6.0
Release:       %mkrel 2
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.sourceforge.net/
License:	   GPL

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Obsoletes:	   ispell-%{languagecode}, iirish, ispell-gaeilge

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

cp doc/README README.%{languagecode}
chmod 644 README* Copyright doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright 
%{_libdir}/aspell-%{aspell_ver}/*


