#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-derby
Version  : 10.12.1.1
Release  : 2
URL      : https://github.com/apache/derby/archive/10.12.1.1.tar.gz
Source0  : https://github.com/apache/derby/archive/10.12.1.1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/derby/derby-project/10.12.1.1/derby-project-10.12.1.1.pom
Source2  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.jar
Source3  : https://repo1.maven.org/maven2/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-derby-data = %{version}-%{release}

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


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.12.1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.12.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/derby/derby-project/10.12.1.1/derby-project-10.12.1.1.pom
/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.jar
/usr/share/java/.m2/repository/org/apache/derby/derby/10.12.1.1/derby-10.12.1.1.pom
