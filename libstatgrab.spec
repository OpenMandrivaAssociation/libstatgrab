%define sname	statgrab
%define major	6
%define libname	%mklibname %{sname} %major
%define devname	%mklibname -d %{sname}

Summary:	Make system statistics
Name:		libstatgrab
Version:	0.17
Release:	4
License:	LGPLv2+
Group:		Monitoring
Url:		http://www.i-scream.org/libstatgrab/
Source0:	ftp://ftp.uk.i-scream.org/pub/i-scream/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}.nochmod.patch

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

%package -n %{sname}-tools
Summary:	Tools from %{name} to monitoring the system
Group:		Monitoring
License:	GPLv2+

%description -n %{sname}-tools
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

%package -n %{libname}
Summary:	The %{name} libraries
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	The development files from %{name} libraries
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std

%files -n %{sname}-tools
%doc AUTHORS INSTALL README ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libstatgrab.so.%{major}*

%files -n %{devname}
%doc AUTHORS INSTALL README ChangeLog NEWS
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*

