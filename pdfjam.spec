Summary:	Utilities for join, rotate and align PDFs
Summary(pl.UTF-8):	Narzędzia do łączenia, rotacji i wyrównywania plików PDF
Name:		pdfjam
Version:	2.08
Release:	1
License:	GPL v2
Group:		Applications/Printing
Source0:	http://www.warwick.ac.uk/go/pdfjam/%{name}_208.tgz
# Source0-md5:	7df075df7f129091f826275ce8c1f374
URL:		http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic/firth/software/pdfjam/
Requires:	tetex-format-pdflatex
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDFjam is a small collection of shell scripts which provide a simple
interface to some of the functionality of the excellent pdfpages
package (by Andreas Matthias) for pdfLaTeX. At present the utilities
available are:
- pdfnup, which allows PDF files to be "n-upped" in roughly the way
  that psnup does for PostScript files
- pdfjoin, which concatenates the pages of multiple PDF files together
  into a single file
- pdf90, which rotates the pages of one or more PDF files through 90
  degrees (anti-clockwise)

In every case, source files are left unchanged.

%description -l pl.UTF-8
PDFjam jest małym zbiorem skryptów powłoki dostarczających prosty
interfejs do kilku funkcji pdfLaTeXa. W tym momencie dostępne
narzędzia to:
- pdfnup - umożliwia umieszczanie wielu stron PDF na jednej stronie,
  podobnie jak robi to psnup dla PostScriptu,
- pdfjoin - umożliwia łączenie plików PDF w pojedynczy plik,
- pdf90 - pozwala obracać strony w pliku PDF.

Każde z tych narzędzi pozostawia pliki źródłowe niezmienione.

%prep
%setup -q  -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1}
install -p pdfjam.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -p bin/* $RPM_BUILD_ROOT%{_bindir}
install -p man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc pdfdroplets.png PDFjam-README.html VERSION
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pdfjam.conf
%attr(755,root,root) %{_bindir}/pdf*
%{_mandir}/man1/pdf*.1*
