#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-ast
Version  : 1.0.16
Release  : 27
URL      : https://pecl.php.net/get/ast-1.0.16.tgz
Source0  : https://pecl.php.net/get/ast-1.0.16.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-ast-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
php-ast
=======
This extension exposes the abstract syntax tree generated by PHP 7.

%package lib
Summary: lib components for the php-ast package.
Group: Libraries

%description lib
lib components for the php-ast package.


%prep
%setup -q -n ast-1.0.16
cd %{_builddir}/ast-1.0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/ast.so
