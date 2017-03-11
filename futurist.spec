#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : futurist
Version  : 0.21.0
Release  : 30
URL      : http://tarballs.openstack.org/futurist/futurist-0.21.0.tar.gz
Source0  : http://tarballs.openstack.org/futurist/futurist-0.21.0.tar.gz
Source99 : http://tarballs.openstack.org/futurist/futurist-0.21.0.tar.gz.asc
Summary  : Useful additions to futures, from the future.
Group    : Development/Tools
License  : Apache-2.0
Requires: futurist-python
Requires: contextlib2
Requires: futures
Requires: monotonic
Requires: pbr
Requires: six
BuildRequires : contextlib2-python
BuildRequires : eventlet-python
BuildRequires : funcsigs-python
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : monotonic-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : reno-python
BuildRequires : setuptools
BuildRequires : testrepository-python
BuildRequires : tox
BuildRequires : virtualenv

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/futurist.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package python
Summary: python components for the futurist package.
Group: Default

%description python
python components for the futurist package.


%prep
%setup -q -n futurist-0.21.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489274237
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1489274237
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
