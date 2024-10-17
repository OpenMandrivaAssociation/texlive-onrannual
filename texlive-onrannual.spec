Name:		texlive-onrannual
Version:	17474
Release:	2
Summary:	Class for Office of Naval Research Ocean Battlespace Sensing annual report
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/onrannual
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onrannual.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onrannual.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an unofficial document class for writing ONR annual
reports using LaTeX; as ONR has had numerous problems with
LaTeX-generated PDF submissions in the past. A skeleton
document (and its PDF output) are included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/onrannual/onrannual.cls
%doc %{_texmfdistdir}/doc/latex/onrannual/README
%doc %{_texmfdistdir}/doc/latex/onrannual/sample.bib
%doc %{_texmfdistdir}/doc/latex/onrannual/samplefigure.eps
%doc %{_texmfdistdir}/doc/latex/onrannual/samplefigure.pdf
%doc %{_texmfdistdir}/doc/latex/onrannual/skeleton.pdf
%doc %{_texmfdistdir}/doc/latex/onrannual/skeleton.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
