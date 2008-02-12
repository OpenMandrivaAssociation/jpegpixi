Summary:	Command line tool to fix bad pixels in digital photos
Name:		jpegpixi
Version:	1.1.1
Release:	%mkrel 1
License:	GPL
Group:		Graphics

Source:		http://www.zero-based.org/software/jpegpixi/%{name}-%{version}.tar.bz2

Url:		http://www.zero-based.org/software/jpegpixi/
#Url:		http://jpegpixi.sourceforge.net/
#Url:		http://sourceforge.net/projects/jpegpixi/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	libjpeg-devel

%description
"Jpegpixi" is short for "JPEG pixel interpolator". The intent of the
program is to interpolate pixels in JFIF images (commonly referred to
as "JPEG images"). This is useful to correct images from a digital
camera with CCD defects. For example, if one pixel is always bright
green, this pixel can be interpolated away with jpegpixi.

Jpegpixi is unique in that it tries to preserve the quality of the
JFIF image as much as possible. Usual graphics programs decode JFIF
images when they are loaded, and re-encode them when they are saved,
which results in an overall loss of quality. Jpegpixi, on the other
hand, does not decode and re-encode the image, but manipulates the
encoded image data (known as the "DCT coefficients"). Therefore, the
blocks (typically 8×8, 8×16, or 16×16 pixel areas) which contain the
pixels to be interpolated are minimally disturbed, whereas other
blocks remain pixel-by-pixel identical to the original image.

Jpegpixi is a command line utility. It is Free Software, released
under the GNU General Public License.

Please read the manual page for detailed usage instructions ("man
jpegpixi"). For a usage example, please see the "Example" section on
the jpegpixi homepage at <http://jpegpixi.sourceforge.net/>.


%prep

%setup -q

%build
%configure
%make

%install
%makeinstall

%find_lang %name

%clean
rm -fr %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.jpeglib
%_bindir/*
%_mandir/*/*
