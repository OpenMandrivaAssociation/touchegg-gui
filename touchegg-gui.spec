Name:		touchegg-gui
Version:	0.3
Release:	1
Summary:	Touchegg configuration gui
License:	GPLv3
Group:		System/Configuration/Hardware
Source0:	https://touchegg.googlecode.com/files/%{name}-%{version}.tar.gz
Url:		https://code.google.com/p/touchegg
Patch0:		%{name}-0.3-desktopfile.patch
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	desktop-file-utils
Requires:	touchegg

%description
Graphical user interface that helps configuring touchegg

%prep
%setup -q -n %{name}
%patch0 -p1 -b .desktopfile

%build
%qmake_qt4
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}
chmod a-x %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
