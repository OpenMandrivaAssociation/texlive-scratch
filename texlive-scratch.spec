%global tl_name scratch
%global tl_revision 66655

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.41
Release:	%{tl_revision}.1
Summary:	Draw programs like scratch
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/macros/latex/contrib/scratch
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scratch.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is now obsolete. From now on, scratch at scratch.mit.edu is
now version3 with a new design. Please, use the "scratch3" package to
draw blocks with the new design. This package permits to draw program
charts in the style of the scatch project (scratch.mit.edu). It depends
on the other LaTeX packages TikZ and simplekv.

