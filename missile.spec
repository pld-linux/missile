Summary:	A clone of the Atari Missile Command
Summary(pl):	Klon atarowskiej gry Missile Command
Name:		missile
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://missile.sourceforge.net/dl/%{name}-%{version}.tar.gz
# Source0-md5:	df91618f5ea46e5c9e8a395273b85e01
URL:		http://missile.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A clone of the Atari Missile Command.

%description -l pl
Klon atarowskiej gry Missile Command.

%prep
%setup -q

%build
%{__make} game_prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/missile,%{_pixmapsdir},%{_applnkdir}/Games/Arcade}

install missile $RPM_BUILD_ROOT%{_bindir}
mv data/{graphics,sound} $RPM_BUILD_ROOT%{_datadir}/missile
install data/missile_icon.png $RPM_BUILD_ROOT%{_datadir}/missile
install icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
install missile.desktop $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/missile
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/*
