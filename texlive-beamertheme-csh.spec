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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Beamer theme following the corporate design of
the Complexity Science Hub (CSH) Vienna. It includes a title page,
automatic section slides, source citation commands, and a closing slide
with QR code. The theme uses TeX Gyre Heros as the default font.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-csh
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-csh
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-csh/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-csh/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-csh/example-csh.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-csh/example-csh.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-csh/beamercolorthemecsh.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-csh/beamerinnerthemecsh.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-csh/beamerouterthemecsh.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-csh/beamerthemecsh.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-csh/csh-logo-star-crop.pdf
%{_datadir}/texmf-dist/tex/latex/beamertheme-csh/csh-logo-web.pdf
