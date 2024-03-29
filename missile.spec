Summary:	A clone of the Atari Missile Command
Summary(pl.UTF-8):	Klon atarowskiej gry Missile Command
Name:		missile
Version:	1.0.1
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://missile.sourceforge.net/dl/%{name}-%{version}.tar.gz
# Source0-md5:	a4a429dc74efff08ab555c792957fe4a
Patch0:		%{name}-ldflags.patch
Patch1:		%{name}-desktop.patch
URL:		http://missile.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A clone of the Atari Missile Command.

%description -l pl.UTF-8
Klon atarowskiej gry Missile Command.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	game_prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/missile,%{_pixmapsdir},%{_desktopdir}}

install missile $RPM_BUILD_ROOT%{_bindir}
mv data/{graphics,sound} $RPM_BUILD_ROOT%{_datadir}/missile
install data/missile_icon.png $RPM_BUILD_ROOT%{_datadir}/missile
install icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
install missile.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/missile
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
