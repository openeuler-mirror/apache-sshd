Epoch:               1
Name:                apache-sshd
Version:             2.2.0
Release:             1
Summary:             Apache SSHD
License:             ASL 2.0 and ISC
URL:                 http://mina.apache.org/sshd-project
Source0:             https://archive.apache.org/dist/mina/sshd/%{version}/apache-sshd-%{version}-src.tar.gz
Patch0:              0001-Avoid-optional-dependency-on-native-tomcat-APR-libra.patch
BuildRequires:       maven-local mvn(junit:junit) mvn(net.i2p.crypto:eddsa) mvn(org.apache.ant:ant)
BuildRequires:       mvn(org.apache:apache:pom:) mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.maven:maven-archiver)
BuildRequires:       mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:       mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires:       mvn(org.bouncycastle:bcpg-jdk15on) mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:       mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:       mvn(org.codehaus.plexus:plexus-archiver) mvn(org.slf4j:slf4j-api)
BuildArch:           noarch
%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.

%package        javadoc
Summary:             API documentation for %{name}
%description    javadoc
This package provides %{name}.

%prep
%setup -q
%patch0 -p1
rm -rf sshd-core/src/main/java/org/apache/sshd/agent/unix
%pom_remove_dep :spring-framework-bom
%pom_disable_module assembly
%pom_disable_module sshd-mina
%pom_disable_module sshd-netty
%pom_disable_module sshd-ldap
%pom_disable_module sshd-git
%pom_disable_module sshd-contrib
%pom_disable_module sshd-spring-sftp
%pom_disable_module sshd-cli
%pom_disable_module sshd-openpgp
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :groovy-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_xpath_inject "pom:configuration/pom:instructions" "<_nouses>true</_nouses>" .

%build
%mvn_build -f -- -Dworkspace.root.dir=$(pwd)

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%changelog
* Thu Aug 6 2020 Jeffery.Gao <gaojianxing@huawei.com> - 2.2.0-1
- Package init
