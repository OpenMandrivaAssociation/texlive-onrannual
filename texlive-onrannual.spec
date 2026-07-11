%global tl_name onrannual
%global tl_revision 17474

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Class for Office of Naval Research Ocean Battlespace Sensing annual report
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/onrannual
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/onrannual.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/onrannual.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an unofficial document class for writing ONR annual reports
using LaTeX; as ONR has had numerous problems with LaTeX-generated PDF
submissions in the past. A skeleton document (and its PDF output) are
included.

