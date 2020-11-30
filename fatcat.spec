Name:           fatcat
Version:        1.1.0
Release:        1%{?dist}
Summary:        FAT explore, extract, repair and forensic tool

License:        MIT
URL:            https://github.com/Gregwar/fatcat
Source0:        https://github.com/Gregwar/fatcat/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Fatcat is a standalone tool that allow you to explore, extract, repair and
forensic FAT filesystems. It currently supports FAT12, FAT16 and FAT32.

%prep
%autosetup

%build
%cmake
%make_build

%install
%make_install
install -Dpm644 man/fatcat.1 %{buildroot}%{_mandir}/man1/fatcat.1

%files
%license LICENSE
%doc README.md
%{_bindir}/fatcat
%{_mandir}/man1/fatcat.1*
%doc docs/*

%changelog
* Mon Nov 30 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.1.0-1
- Initial package
