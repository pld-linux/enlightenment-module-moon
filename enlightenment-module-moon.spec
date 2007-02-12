%define		_module_name	moon

Summary:	Enlightenment DR17 module: Moon
Summary(pl.UTF-8):   Moduł Enlightenmenta DR17: Moon
Name:		enlightenment-module-%{_module_name}
Version:	0.0.2
Release:	1
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
# Source0-md5:	1df53fb8da941049acb800445f4ad13f
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenmentDR17-devel
BuildRequires:	libtool
Requires:	enlightenmentDR17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment DR17 module showing current phase of the Moon.

%description -l pl.UTF-8
Moduł Enlightenmenta DR17 pokazujący aktualną fazę Księżyca.

%prep
%setup -q -n %{_module_name}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--prefix=`enlightenment-config --module-dir`
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL README TODO
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
# violates FHS
%{_libdir}/enlightenment/modules_extra/%{_module_name}/%{_module_name}.*
#%{_libdir}/enlightenment/modules_extra/%{_module_name}/module_icon.png
