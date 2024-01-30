#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-ast
Version  : 1.1.1
Release  : 72
URL      : https://pecl.php.net/get/ast-1.1.1.tgz
Source0  : https://pecl.php.net/get/ast-1.1.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-ast-lib = %{version}-%{release}
Requires: php-ast-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n ast-1.1.1
cd %{_builddir}/ast-1.1.1
pushd ..
cp -a ast-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-ast
cp %{_builddir}/ast-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-ast/2253d606a560921b22289386ab37dd7317ad90a0 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/ast.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-ast/2253d606a560921b22289386ab37dd7317ad90a0
