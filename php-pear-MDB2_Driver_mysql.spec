%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	MDB2_Driver_mysql
%define		subver	b3
%define		rel		3
Summary:	%{_pearname} - mysql MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik mysql dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	0.%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	b10ae9cb1dd304678879dd5e4533a031
URL:		http://pear.php.net/package/MDB2_Driver_mysql/
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php(mysql)
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:1.5.0-0.b3
Obsoletes:	php-pear-MDB2_Driver_mysql-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the MySQL MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik MySQL dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/mysql.php
%{php_pear_dir}/MDB2/Driver/Manager/mysql.php
%{php_pear_dir}/MDB2/Driver/Native/mysql.php
%{php_pear_dir}/MDB2/Driver/Reverse/mysql.php
%{php_pear_dir}/MDB2/Driver/mysql.php
%{php_pear_dir}/MDB2/Driver/Function/mysql.php
%{php_pear_dir}/data/MDB2_Driver_mysql
