Summary:	DevHelp book: emacs
Summary(pl):	Ksi±¿ka do DevHelp'a o emacs
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

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about emacs

%description -l pl
Ksi±¿ka do DevHelp o emacs

%prep
%setup -q -c emacs -n emacs

%build
mv -f book emacs-13.0
mv -f book.devhelp emacs.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/emacs-13.0
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install emacs.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install emacs-13.0/* $RPM_BUILD_ROOT%{_prefix}/books/emacs-13.0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
