#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-derby
Version  : 10.12.1.1
Release  : 3
URL      : https://github.com/apache/derby/archive/10.12.1.1.tar.gz
Source0  : https://github.com/apache/derby/archive/10.12.1.1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/derby/derby-project/10.12.1.1/derby-project-10.12.1.1.pom
Source2  : https://repo1.maven.org/maven2/org/apache/derby/derby-project/10.14.2.0/derby-project-10.14.2.0.pom
Source3  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.jar
Source4  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.pom
Source5  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.14.2.0/derby-10.14.2.0.jar
Source6  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.14.2.0/derby-10.14.2.0.pom
Source7  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.4.2.0/derby-10.4.2.0.jar
Source8  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.4.2.0/derby-10.4.2.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-derby-data = %{version}-%{release}
Requires: mvn-derby-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
<!--
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to you under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

%package data
Summary: data components for the mvn-derby package.
Group: Data

%description data
data components for the mvn-derby package.


%package license
Summary: license components for the mvn-derby package.
Group: Default

%description license
license components for the mvn-derby package.


%prep
%setup -q -n derby-10.12.1.1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-derby
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-derby/LICENSE
cp plugins/eclipse/org.apache.derby.plugin.doc/LICENSE %{buildroot}/usr/share/package-licenses/mvn-derby/plugins_eclipse_org.apache.derby.plugin.doc_LICENSE
cp plugins/eclipse/org.apache.derby.ui/LICENSE %{buildroot}/usr/share/package-licenses/mvn-derby/plugins_eclipse_org.apache.derby.ui_LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.12.1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.12.1.1/derby-project-10.12.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.14.2.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.14.2.0/derby-project-10.14.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.14.2.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.14.2.0/derby-10.14.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.14.2.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.14.2.0/derby-10.14.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.4.2.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.4.2.0/derby-10.4.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.4.2.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.4.2.0/derby-10.4.2.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.12.1.1/derby-project-10.12.1.1.pom
/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.14.2.0/derby-project-10.14.2.0.pom
/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.jar
/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.pom
/usr/share/java/.m2/repository/org/apache/derby/derby/10.14.2.0/derby-10.14.2.0.jar
/usr/share/java/.m2/repository/org/apache/derby/derby/10.14.2.0/derby-10.14.2.0.pom
/usr/share/java/.m2/repository/org/apache/derby/derby/10.4.2.0/derby-10.4.2.0.jar
/usr/share/java/.m2/repository/org/apache/derby/derby/10.4.2.0/derby-10.4.2.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-derby/LICENSE
/usr/share/package-licenses/mvn-derby/plugins_eclipse_org.apache.derby.plugin.doc_LICENSE
/usr/share/package-licenses/mvn-derby/plugins_eclipse_org.apache.derby.ui_LICENSE
