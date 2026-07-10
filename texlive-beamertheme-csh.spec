%global tl_name beamertheme-csh
%global tl_revision 76967

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A Beamer presentation theme for the Complexity Science Hub Vienna
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-csh
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-csh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-csh.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Beamer theme following the corporate design of
the Complexity Science Hub (CSH) Vienna. It includes a title page,
automatic section slides, source citation commands, and a closing slide
with QR code. The theme uses TeX Gyre Heros as the default font.

