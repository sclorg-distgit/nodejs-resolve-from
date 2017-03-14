%{?scl:%scl_package nodejs-resolve-from}
%{!?scl:%global pkg_name %{name}}

%global npm_name resolve-from
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-resolve-from
Version:	2.0.0
Release:	1%{?dist}
Summary:	Resolve the path of a module like require.resolve() but from a given path
Url:		https://github.com/sindresorhus/resolve-from
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

# tests are turned off because of missing dependencies
%if 0%{?enable_tests}
BuildRequires:	npm(ava)
BuildRequires:	npm(xo)
%endif

%description
Resolve the path of a module like require.resolve() but from a given path

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
xo && ava
%endif

%files
%{nodejs_sitelib}/resolve-from

%doc readme.md
%doc license

%changelog
* Sun Apr 03 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-1
- Initial build
