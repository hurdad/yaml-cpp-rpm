Name:           yaml-cpp
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        A YAML parser and emitter in C++
Group:          System Environment/Libraries
License:	MIT
URL:            https://github.com/jbeder/yaml-cpp
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3

%description
A YAML parser and emitter in C++

%package devel
Summary:	%{name} development package
Group:		Development/Libraries

%description devel
Development files for %{name}.

%prep
%setup -n %{name}-%{name}-%{version}

%build
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DBUILD_SHARED_LIBS=ON -DYAML_CPP_BUILD_TESTS=OFF
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md 
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%changelog
