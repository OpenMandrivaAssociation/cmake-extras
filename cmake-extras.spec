Summary:    A collection of add-ons for the CMake build tool
Name:       cmake-extras
Version:    1.8
Release:    1
License:    GPL-3.0
Group:		Development/Other
URL:        https://gitlab.com/ubports/development/core/cmake-extras
Source0:    https://gitlab.com/ubports/development/core/cmake-extras/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: ninja
BuildRequires: python

Requires:      intltool
Requires:      gettext
Requires:      gtest-source
Requires:      lcov
Requires:      qt5-qtdeclarative

BuildArch:  noarch

%description
A collection of add-ons for the CMake build tool.

%files
%license LICENSE
%{_datadir}/cmake/CopyrightTest/CopyrightTestConfig.cmake
%{_datadir}/cmake/CopyrightTest/check_copyright.sh
%{_datadir}/cmake/CoverageReport/CoverageReportConfig.cmake
%{_datadir}/cmake/CoverageReport/EnableCoverageReport.cmake
%{_datadir}/cmake/DoxygenBuilder/Doxyfile.in
%{_datadir}/cmake/DoxygenBuilder/DoxygenBuilderConfig.cmake
%{_datadir}/cmake/GDbus/GDbusConfig.cmake
%{_datadir}/cmake/GMock/GMockConfig.cmake
%{_datadir}/cmake/GSettings/GSettingsConfig.cmake
%{_datadir}/cmake/Intltool/IntltoolConfig.cmake
%{_datadir}/cmake/Lcov/LcovConfig.cmake
%{_datadir}/cmake/QmlPlugins/QmlPluginsConfig.cmake
%{_datadir}/cmake/FormatCode/unity-api.clang-format
%{_datadir}/cmake/FormatCode/formatcode.in
%{_datadir}/cmake/FormatCode/formatcode_format.cmake.in
%{_datadir}/cmake/FormatCode/unity-api.astyle
%{_datadir}/cmake/FormatCode/formatcode_test.cmake.in
%{_datadir}/cmake/FormatCode/FormatCodeConfig.cmake
%{_datadir}/cmake/FormatCode/formatcode_common.cmake
%{_datadir}/cmake/gcovr/gcovrConfig.cmake
%{_datadir}/cmake/IncludeChecker/IncludeCheckerConfig.cmake
%{_datadir}/cmake/IncludeChecker/deps
%{_datadir}/cmake/IncludeChecker/include_checker.py
%{_datadir}/cmake/GObjectIntrospection/GObjectIntrospectionConfig.cmake
%{_datadir}/cmake/GdbusCodegen/GdbusCodegenConfig.cmake
%{_datadir}/cmake/Vala/ValaConfig.cmake

#-----------------------------------------------------------------------

%prep
%autosetup -p1
sed -i 's/#!\/bin\/sh/#!\/usr\/bin\/sh/' src/FormatCode/formatcode.in
sed -i 's/#!\/bin\/sh/#!\/usr\/bin\/sh/' src/CopyrightTest/check_copyright.sh
sed -i 's/python/python3/' src/IncludeChecker/include_checker.py
sed -i 'sX/usr/lib/qt5X${CMAKE_LIBDIR}/qt5X' src/QmlPlugins/QmlPluginsConfig.cmake

%build
%cmake \
	-GNinja
%ninja_build

%install
%ninja_install -C build

# Correct this as we actually don't have a gmock source dir
#rm {buildroot}/usr/share/cmake/GMock/GMockConfig.cmake
#cp {SOURCE1} {buildroot}/usr/share/cmake/GMock/


