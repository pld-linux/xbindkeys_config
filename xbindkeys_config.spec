Summary:	An easy to use gtk program for configuring xbindkeys
Summary(pl):	Prosty program do konfiguracji programu xbindkeys
Name:		xbindkeys_config
Version:	0.1.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.netchampagne.com/xbindkeys_config/%{name}-%{version}.tar.gz
URL:		http://www.netchampagne.com/xbindkeys_config/
BuildRequires:	gtk+-devel
Requires:	xbindkeys
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An easy to use gtk program for configuring xbindkeys.

%description -l pl
Prosty program do konfiguracji programu xbindkeys.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/xbindkeys_config
