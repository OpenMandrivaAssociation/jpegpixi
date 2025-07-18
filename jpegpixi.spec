Summary:	Command line tool to fix bad pixels in digital photos
Name:		jpegpixi
Version:	1.1.1
Release:	7
License:	GPLv2+
Group:		Graphics
Url:		https://www.zero-based.org/software/jpegpixi/
Source0:	http://www.zero-based.org/software/jpegpixi/%{name}-%{version}.tar.bz2
BuildRequires:	jpeg-devel

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
blocks (typically 8x8, 8x16, or 16x16 pixel areas) which contain the
pixels to be interpolated are minimally disturbed, whereas other
blocks remain pixel-by-pixel identical to the original image.

Jpegpixi is a command line utility. It is Free Software, released
under the GNU General Public License.

Please read the manual page for detailed usage instructions ("man
jpegpixi"). For a usage example, please see the "Example" section on
the jpegpixi homepage at <http://jpegpixi.sourceforge.net/>.

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README README.jpeglib
%{_bindir}/jpeghotp
%{_bindir}/jpegpixi
%{_mandir}/man1/jpeghotp.1*
%{_mandir}/man1/jpegpixi.1*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} jpeghotp %{name}.lang --with-man

