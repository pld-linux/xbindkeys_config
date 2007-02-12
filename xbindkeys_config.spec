Summary:	An easy to use GTK+ program for configuring xbindkeys
Summary(pl.UTF-8):	Prosty program do konfiguracji programu xbindkeys
Name:		xbindkeys_config
Version:	0.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.netchampagne.com/xbindkeys_config/%{name}-%{version}.tar.gz
# Source0-md5:	c8983fd822e66c9f9bfbe5e99044a203
URL:		http://www.netchampagne.com/xbindkeys_config/
BuildRequires:	gtk+-devel
Requires:	xbindkeys
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An easy to use GTK+ program for configuring xbindkeys.

%description -l pl.UTF-8
Prosty program do konfiguracji programu xbindkeys.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} -Wall"

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
