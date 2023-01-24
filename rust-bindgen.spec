# Generated by rust2rpm 11
%bcond_without check

%global crate bindgen

Name:           rust-%{crate}
Version:        0.63.0
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://crates.io/crates/bindgen
#Source:         %{crates_source}
Source0:      https://github.com/rust-lang/rust-bindgen/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

ExclusiveArch:  %{rust_arches}
#if %{__cargo_skip_build}
BuildArch:      noarch
#endif

BuildRequires:  rust-packaging

%global _description %{expand:
Automatically generates Rust FFI bindings to C and C++ libraries.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/bindgen
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages
which use "clap" feature of "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+env_logger-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+env_logger-devel %{_description}

This package contains library source intended for building other packages
which use "env_logger" feature of "%{crate}" crate.

%files       -n %{name}+env_logger-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages
which use "logging" feature of "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-devel %{_description}

This package contains library source intended for building other packages
which use "runtime" feature of "%{crate}" crate.

%files       -n %{name}+runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages
which use "static" feature of "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+testing_only_docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_docs-devel %{_description}

This package contains library source intended for building other packages
which use "testing_only_docs" feature of "%{crate}" crate.

%files       -n %{name}+testing_only_docs-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+testing_only_extra_assertions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_extra_assertions-devel %{_description}

This package contains library source intended for building other packages
which use "testing_only_extra_assertions" feature of "%{crate}" crate.

%files       -n %{name}+testing_only_extra_assertions-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+testing_only_libclang_3_8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_libclang_3_8-devel %{_description}

This package contains library source intended for building other packages
which use "testing_only_libclang_3_8" feature of "%{crate}" crate.

%files       -n %{name}+testing_only_libclang_3_8-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+testing_only_libclang_3_9-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_libclang_3_9-devel %{_description}

This package contains library source intended for building other packages
which use "testing_only_libclang_3_9" feature of "%{crate}" crate.

%files       -n %{name}+testing_only_libclang_3_9-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+testing_only_libclang_4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_libclang_4-devel %{_description}

This package contains library source intended for building other packages
which use "testing_only_libclang_4" feature of "%{crate}" crate.

%files       -n %{name}+testing_only_libclang_4-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+testing_only_libclang_5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_libclang_5-devel %{_description}

This package contains library source intended for building other packages
which use "testing_only_libclang_5" feature of "%{crate}" crate.

%files       -n %{name}+testing_only_libclang_5-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+testing_only_libclang_9-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_libclang_9-devel %{_description}

This package contains library source intended for building other packages
which use "testing_only_libclang_9" feature of "%{crate}" crate.

%files       -n %{name}+testing_only_libclang_9-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+which-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+which-devel %{_description}

This package contains library source intended for building other packages
which use "which" feature of "%{crate}" crate.

%files       -n %{name}+which-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+which-rustfmt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+which-rustfmt-devel %{_description}

This package contains library source intended for building other packages
which use "which-rustfmt" feature of "%{crate}" crate.

%files       -n %{name}+which-rustfmt-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -p 1 -a 1
install -D -m 0644 %{SOURCE2} .cargo/config

#generate_buildrequires
#cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 14:57:26 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.52.0-1
- Update to 0.52.0

* Wed Jul 31 18:31:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.51.0-1
- Release 0.51.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.49.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 08:38:03 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.0-3
- Update hashbrown to 0.3

* Sun Apr 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.49.0-2
- Rebuilt for hashbrown 0.2.0

* Wed Mar 27 2019 Josh Stone <jistone@redhat.com> - 0.49.0-1
- Update to 0.49.0

* Sat Mar 16 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.48.1-1
- Update to 0.48.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Josh Stone <jistone@redhat.com> - 0.47.0-1
- Update to 0.47.0

* Mon Jan 14 2019 Josh Stone <jistone@redhat.com> - 0.46.0-1
- Update to 0.46.0

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.43.1-1
- Update to 0.43.1

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.43.0-2
- Adapt to new packaging

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.43.0-1
- Update to 0.43.0

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 0.42.2-1
- Update to 0.42.2

* Mon Oct 08 2018 Josh Stone <jistone@redhat.com> - 0.42.1-1
- Update to 0.42.1

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.42.0-1
- Initial package
