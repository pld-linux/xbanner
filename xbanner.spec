Summary:	A program for customizing the look of the standard XDM interface
Summary(pl):	Program do konfigurowania wygl±du XDM
Name:		xbanner
Version:	1.31
Release:	7
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://physics.fullerton.edu/pub/Linux/XBanner/XBanner%{version}.tar.gz
Patch0:		%{name}-1.3-rh.patch
Patch1:		%{name}-install.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
The XBanner program allows the display of text, patterns and images in
the root window, so users can customize the XDM style login screen
and/or the normal X background.

Install XBanner if you'd like to change the look of your X login
screen and/or X background.

%description -l pl
Program XBanner pozwala wy¶wietlaæ teksty, wzory i obrazki w g³ównym
oknie, tak, ¿e u¿ytkownicy mog± konfigurowaæ ekran logowania XDM oraz
zwyk³e t³o X.

%prep
%setup -q -n XBanner1.31
%patch0 -p1
%patch1 -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/X11/pixmaps,%{_libdir}/X11/app-defaults}

# we stuck xsri in here for now, move it out after 6.0 to separate package
%{__make} install ROOT="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc samples docs/*
%attr(755,root,root) %{_bindir}/freetemp
%attr(755,root,root) %{_bindir}/xbanner
%attr(755,root,root) %{_bindir}/xb_check
