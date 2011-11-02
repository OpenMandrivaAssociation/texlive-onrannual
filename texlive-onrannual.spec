Name:		texlive-onrannual
Version:	1.1
Release:	1
Summary:	Class for Office of Naval Research Ocean Battlespace Sensing annual report
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/onrannual
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onrannual.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/onrannual.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is an unofficial document class for writing ONR annual
reports using LaTeX; as ONR has had numerous problems with
LaTeX-generated PDF submissions in the past. A skeleton
document (and its PDF output) are included.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
