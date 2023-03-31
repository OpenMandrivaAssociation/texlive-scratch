Name:		texlive-scratch
Version:	50073
Release:	2
Summary:	Draw programs like "scratch"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scratch
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is now obsolete. From now on, scratch at
scratch.mit.edu is now version3 with a new design. Please, use
the "scratch3" package to draw blocks with the new design. This
package permits to draw program charts in the style of the
scatch project (scratch.mit.edu). It depends on the other LaTeX
packages TikZ and simplekv.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/scratch
%doc %{_texmfdistdir}/doc/latex/scratch

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
