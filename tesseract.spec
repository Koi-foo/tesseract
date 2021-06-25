Name: tesseract
Version: 4.1.1
Release: alt1

License: ASL 2.0
Group: Graphics
Url: https://github.com/tesseract-ocr
Packager: Koi <eg.evgeniy at gmail.com>

Source0: %{name}-%{version}.tar.gz
Source1: tessdata-fast-ru-en.tar.gz

# For compatibility with third party language packs, configure the location of the tessdata folder inside tesseract
Patch0: tesseract_datadir.patch

# Automatically added by buildreq on Mon May 31 2021
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 leptonica libcairo-devel libfreetype-devel libharfbuzz-devel libicu-devel libstdc++-devel perl pkg-config python-base sh4
# BuildRequires: gcc-c++ leptonica-devel libpango-devel libtiff-devel

BuildRequires: gcc-c++ libleptonica-devel libpango-devel libtiff-devel libcairo-devel
BuildRequires: libicu-devel

Requires: libleptonica >= 1.74.2
Requires: tesseract-langpack-en
Requires: tesseract-langpack-ru

Summary: Raw Open source OCR Engine
Summary(ru_RU.UTF-8): Библиотека для манипулирования изображениями

%description
A commercial quality OCR engine originally developed at HP between 1985
and 1995. In 1995, this engine was among the top 3 evaluated by UNLV. It
was open-sourced by HP and UNLV in 2005. From 2007 it is developed by
Google.

%description -l ru_RU.UTF-8
Коммерческий качественный OCR-движок, первоначально разработанный в HP в период
с 1985 по 1995 год. В 1995 году этот движок входил в топ-3, оцененный UNLV. Он
был открыт HP и UNLV в 2005 году. С 2007 года он разрабатывается
Google.


%package devel
Summary: Development files for %{name}
Summary(ru_RU.UTF-8): Файлы разработки для %{name}
Group: Development/C
Requires: %name = %version-%release

%description devel
The %{name}-devel package contains header file for
developing applications that use %{name}.

%description -l ru_RU.UTF-8 devel
Пакет %{name}-devel содержит файл заголовка для
разработки приложений, использующих %{name}.


%package tools
Summary: Training tools for %{name}
Summary(ru_RU.UTF-8): Обучающие инструменты для %{name}
Group: Development/Tools
Requires: %name = %version-%release

%description tools
The %{name}-tools package contains tools for training %{name}.

%description -l ru_RU.UTF-8 tools
Пакет %{name}-tools содержит инструменты для обучения %{name}.


%package langpack-en
Group: Graphics
Summary: English language pack for tesseract
Summary(ru_RU.UTF-8): Английский языковой пакет для tesseract
Requires: tesseract >= 4.0.0
Provides: tesseract-eng = %version
Obsoletes: tesseract-eng < %version
BuildArch: noarch

%description langpack-en
Data files required to recognize English OCR.

%description -l ru_RU.UTF-8 langpack-en
Файлы данных, необходимые для распознавания английского OCR.


%package langpack-ru
Group: Graphics
Summary: Russian language pack for tesseract
Summary(ru_RU.UTF-8): Пакет русского языка для tesseract
Requires: tesseract >= 4.0.0
Provides: tesseract-rus = %version
Obsoletes: tesseract-rus < %version
BuildArch: noarch

%description langpack-ru
Data files required to recognize Russian OCR.

%description -l ru_RU.UTF-8 langpack-ru
Файлы данных, необходимые для распознавания русского OCR.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --disable-static
%make_build
%make_build training

%install
%makeinstall_std
%makeinstall_std training-install

rm -f %{buildroot}%{_libdir}/*.la

# Create directory for tessdata
mkdir -p %{buildroot}/%{_datadir}/%{name}/tessdata/
# In order to save space in the club's repository, only 2 language engines have been collected
tar -xf %SOURCE1 -C %{buildroot}/%{_datadir}/%{name}/tessdata

%files
%doc AUTHORS ChangeLog README.md LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/tessdata
%{_datadir}/%{name}/tessdata/configs/
%{_datadir}/%{name}/tessdata/tessconfigs/
%{_datadir}/%{name}/tessdata/pdf.ttf
%{_libdir}/lib%{name}*.so.4*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/*

%files langpack-en
%{_datadir}/%{name}/tessdata/eng.traineddata

%files langpack-ru
%{_datadir}/%{name}/tessdata/rus.traineddata

%changelog
* Mon May 31 2021 Koi <eg.evgeniy at gmail.com> 4.1.1-alt1
- Initial release for ALT Linux Club
