Name: xbanner
Summary: A program for customizing the look of the standard XDM interface.
Version: 1.31
Release: 7
Copyright: GPL
Group: Amusements/Graphics
Source: ftp://physics.fullerton.edu/pub/Linux/XBanner/XBanner1.31.tar.gz
Source2: xsri-1.0.tar.gz
Patch: xbanner-1.3-rh.patch
Buildroot: /var/tmp/xbanner-root

%description
The XBanner program allows the display of text, patterns and images
in the root window, so users can customize the XDM style login screen
and/or the normal X background.

Install XBanner if you'd like to change the look of your X login screen
and/or X background.

%prep
%setup -q -n XBanner1.31 -a 2
%patch -p1 -b .patch

%build
make CFLAGS="$RPM_OPT_FLAGS"
make -C xsri-1.0 CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/include/X11/pixmaps
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

# we stuck xsri in here for now, move it out after 6.0 to separate package
make ROOT="$RPM_BUILD_ROOT" install
make -C xsri-1.0 prefix=$RPM_BUILD_ROOT/usr install
mv xsri-1.0/README xsri-1.0/README.xsri

%clean
rm -rf $RPM_BUILD_ROOT

%files
# I left random_effect out because the default "make install" rule doesn't
# install it

/usr/X11R6/bin/freetemp
/usr/X11R6/bin/xbanner
/usr/X11R6/bin/xb_check
%doc samples docs/*
/usr/bin/xsri
%doc xsri-1.0/README.xsri
