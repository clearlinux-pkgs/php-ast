#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-ast
Version  : 1.1.0
Release  : 53
URL      : https://pecl.php.net/get/ast-1.1.0.tgz
Source0  : https://pecl.php.net/get/ast-1.1.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-ast-lib = %{version}-%{release}
Requires: php-ast-license = %{version}-%{release}
BuildRequires : buildreq-php

%description
php-ast
=======
This extension exposes the abstract syntax tree generated by PHP 7 and 8.

%package lib
Summary: lib components for the php-ast package.
Group: Libraries
Requires: php-ast-license = %{version}-%{release}

%description lib
lib components for the php-ast package.


%package license
Summary: license components for the php-ast package.
Group: Default

%description license
license components for the php-ast package.


%prep
%setup -q -n ast-1.1.0
cd %{_builddir}/ast-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-ast
cp %{_builddir}/ast-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-ast/2253d606a560921b22289386ab37dd7317ad90a0
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/ast.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-ast/2253d606a560921b22289386ab37dd7317ad90a0
