Summary:	A templating language for ruby
Name:		ruby-markaby
Version:	0.4
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/9738/markaby-%{version}.gem
# Source0-md5:	3bf790dc0d15377762e3858c640758ca
Patch0:		%{name}-nogems.patch
URL:		http://markaby.rubyforge.org
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Markaby is a templating language for Ruby, with a plugin for Rails, which allows you to write HTML templates in pure-Ruby (a la Builder.)

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
%patch0 -p1
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/markaby*
%{ruby_ridir}/*
