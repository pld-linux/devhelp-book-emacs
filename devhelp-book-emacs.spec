Summary:	DevHelp book: emacs
Summary(pl):	Ksi±¿ka do DevHelpa o emacsie
Name:		devhelp-book-emacs
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/emacs.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp

%description
DevHelp book about emacs.

%description -l pl
Ksi±¿ka do DevHelpa o emacsie.

%prep
%setup -q -c -n emacs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/emacs-13.0,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/emacs.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/emacs-13.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
