
%define		name			kant-kash
%define		kashdir			%{_datadir}/kash

Name:		%{name}
Group:		Sciences/Mathematics
License:	Proprietary
Summary:	Computational Algebraic Number Theory
Version:	3
Release:	3
Source0:	ftp://ftp.math.tu-berlin.de/pub/algebra/Kant/Kash_3/KASH3-Linux-i686-2008-07-31.tar.bz2
URL:		http://www.math.tu-berlin.de/~kant/kash.html
ExclusiveArch:	%{ix86}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KANT is a software package for mathematicians interested in algebraic number
theory. For those KANT is a tool for sophisticated computations in number
fields, in global function fields, and in local fields.

%prep
%setup -q -n KASH3-Linux-i686-2008-07-31

%build

%install
mkdir -p %{buildroot}%{kashdir}
cp -far * %{buildroot}%{kashdir}
# non-standard/incomplete
rm -fr %{buildroot}%{kashdir}/html/cgi-bin

mkdir -p  %{buildroot}%{_bindir}
pushd  %{buildroot}%{_bindir}
    cat > %{buildroot}%{_bindir}/kash3 << EOF
#!/bin/sh

%{kashdir}/kash3 -l %{kashdir}/lib "\$@"
EOF
    chmod +x %{buildroot}%{_bindir}/kash3
    ln -s kash3 kash
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%dir %{kashdir}
%{kashdir}/*
