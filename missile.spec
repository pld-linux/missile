Summary:	A clone of the Atari Missile Command
Summary(pl):	Klon atarowskiej gry Missile Command
Name:		missile
Version:	0.99.7
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://missile.sourceforge.net/dl/%{name}-%{version}.src.tar.gz
URL:		http://missile.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A clone of the Atari Missile Command.

%description -l pl
Klon atarowskiej gry Missile Command.

%prep
%setup -q -n %{name}

%build
%{__make} game_prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_pixmapsdir},%{_applnkdir}/Games/Arcade}

install missile $RPM_BUILD_ROOT%{_bindir}
install data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s %{_datadir}/missile $RPM_BUILD_ROOT%{_pixmapsdir}/missile
install icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
install missile.desktop $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/*
