%define name libstatgrab
%define version 0.17
%define release %mkrel 1

%define shortname statgrab
%define major 6
%define libname %mklibname %shortname %major
%define libnamedevel %mklibname -d %shortname

Summary: Make system statistics
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.uk.i-scream.org/pub/i-scream/%{name}/%{name}-%{version}.tar.gz
Patch0: %{name}.nochmod.patch
License: LGPLv2+ and GPLv2+
Group: Monitoring
Url: http://www.i-scream.org/libstatgrab/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's run. It's written in C and presents a selection
of useful interfaces which can be used to access key system statistics. The
current list of statistics includes CPU usage, memory utilisation, disk usage,
process counts, network traffic, disk I/O, and more. 

The current list of platforms is Solaris 2.x, Linux, and FreeBSD 4.x/5.x.
The aim is to extend this to include as many operating systems as possible. 

The package also includes a couple of useful tools. The first, saidar,
provides a curses-based interface to viewing the current state of the 
system. The second, statgrab, gives a sysctl-style interface to the
statistics gathered by libstatgrab. This extends the use of libstatgrab
to people writing scripts or anything else that can't easily make C 
function calls. Included with statgrab is a script to generate an MRTG
configuration file to use statgrab. 

%package -n %shortname-tools
Summary: Tools from %name to monitoring the system
Group: Monitoring
License: GPLv2+

%description -n %shortname-tools
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's run. It's written in C and presents a selection
of useful interfaces which can be used to access key system statistics. The
current list of statistics includes CPU usage, memory utilisation, disk usage,
process counts, network traffic, disk I/O, and more. 

The current list of platforms is Solaris 2.x, Linux , and FreeBSD 4.x/5.x.
The aim is to extend this to include as many operating systems as possible. 

The package also includes a couple of useful tools. The first, saidar,
provides a curses-based interface to viewing the current state of the 
system. The second, statgrab, gives a sysctl-style interface to the
statistics gathered by libstatgrab. This extends the use of libstatgrab
to people writing scripts or anything else that can't easily make C 
function calls. Included with statgrab is a script to generate an MRTG
configuration file to use statgrab. 

%package -n %libname
Summary: The %name libraries
Group: System/Libraries
License: LGPLv2+
Provides: %name = %version-%release

%description -n %libname
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's run. It's written in C and presents a selection
of useful interfaces which can be used to access key system statistics. The
current list of statistics includes CPU usage, memory utilisation, disk usage,
process counts, network traffic, disk I/O, and more. 

The current list of platforms is Solaris 2.x, Linux, and FreeBSD 4.x/5.x.
The aim is to extend this to include as many operating systems as possible. 

The package also includes a couple of useful tools. The first, saidar,
provides a curses-based interface to viewing the current state of the 
system. The second, statgrab, gives a sysctl-style interface to the
statistics gathered by libstatgrab. This extends the use of libstatgrab
to people writing scripts or anything else that can't easily make C 
function calls. Included with statgrab is a script to generate an MRTG
configuration file to use statgrab. 

%package -n %libnamedevel
Summary: The development files from %name libraries
Group: Development/Other
License: LGPLv2+
Provides: %name-devel = %version-%release
Requires: %libname = %version

%description -n %libnamedevel
Libstatgrab is a library that provides cross platform access to statistics
about the system on which it's run. It's written in C and presents a selection
of useful interfaces which can be used to access key system statistics. The
current list of statistics includes CPU usage, memory utilisation, disk usage,
process counts, network traffic, disk I/O, and more. 

The current list of platforms is Solaris 2.x, Linux, and FreeBSD 4.x/5.x.
The aim is to extend this to include as many operating systems as possible. 

The package also includes a couple of useful tools. The first, saidar,
provides a curses-based interface to viewing the current state of the 
system. The second, statgrab, gives a sysctl-style interface to the
statistics gathered by libstatgrab. This extends the use of libstatgrab
to people writing scripts or anything else that can't easily make C 
function calls. Included with statgrab is a script to generate an MRTG
configuration file to use statgrab. 

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %shortname-tools
%defattr(-,root,root)
%doc AUTHORS INSTALL README ChangeLog NEWS
%_bindir/*
%_mandir/*/*

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS INSTALL README ChangeLog NEWS
%_libdir/*.so.%{major}*

%files -n %libnamedevel
%defattr(-,root,root)
%doc AUTHORS INSTALL README ChangeLog NEWS
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%_includedir/*.h
%_libdir/pkgconfig/%name.pc
