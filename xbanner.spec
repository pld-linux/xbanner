Summary:	A program for customizing the look of the standard XDM interface
Summary(pl):	Program do konfigurowania wygl±du XDM
Name:		xbanner
Version:	1.31
Release:	9
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://physics.fullerton.edu/pub/Linux/XBanner/XBanner%{version}.tar.gz
# Source0-md5:	df62cd1764b4c298c87f1747b6e82da6
Patch0:		%{name}-1.3-rh.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-nostatic.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	XLIBDIR=/usr/X11R6/%{_lib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc samples docs/{Changes.txt,Credits.txt,*.html,*.gif}
%attr(755,root,root) %{_bindir}/freetemp
%attr(755,root,root) %{_bindir}/xbanner
%attr(755,root,root) %{_bindir}/xb_check
