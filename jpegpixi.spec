Summary:	Command line tool to fix bad pixels in digital photos
Name:		jpegpixi
Version:	1.1.1
Release:	%mkrel 5
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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdv2011.0
+ Revision: 612512
- the mass rebuild of 2010.1 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-4mdv2010.0
+ Revision: 429647
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2009.0
+ Revision: 247421
- rebuild
- fix spacing at top of description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2008.1
+ Revision: 127415
- kill re-definition of %%buildroot on Pixel's request

  + Marcelo Ricardo Leitner <mrl@mandriva.com>
    - Import jpegpixi



* Wed Nov 23 2005 Lenny Cartier <lenny@mandriva.com> 1.1.1-1mdk
- 1.1.1

* Tue Jun 14 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.0-1mdk
- New release 1.1.0

* Mon Oct 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2

* Wed Oct 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Tue Aug 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.16.0-1mdk
- 0.16.0

* Wed May 12 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.15.1-1mdk
- 0.15.1

* Tue Mar 16 2004 Till Kamppeter <till@mandrakesoft.com> 0.14.2-1mdk
- Version 0.14.2

* Tue Dec 16 2003 Till Kamppeter <till@mandrakesoft.com> 0.13-1mdk
- Version 0.13
- Removed explicit library dependency (libjpeg62).

* Wed Aug 20 2003 Till Kamppeter <till@mandrakesoft.com> 0.11-1mdk
- Version 0.11
- New URL

* Sun Jul 27 2003 Till Kamppeter <till@mandrakesoft.com> 0.10-1mdk
- Initial release
