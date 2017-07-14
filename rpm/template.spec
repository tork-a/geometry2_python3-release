Name:           ros-lunar-tf2-ros
Version:        0.5.16
Release:        0%{?dist}
Summary:        ROS tf2_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-actionlib
Requires:       ros-lunar-actionlib-msgs
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-message-filters
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rosgraph
Requires:       ros-lunar-rospy
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-tf2
Requires:       ros-lunar-tf2-msgs
Requires:       ros-lunar-tf2-py
Requires:       ros-lunar-xmlrpcpp
BuildRequires:  ros-lunar-actionlib
BuildRequires:  ros-lunar-actionlib-msgs
BuildRequires:  ros-lunar-catkin >= 0.5.68
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-message-filters >= 1.11.1
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rosgraph
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf2
BuildRequires:  ros-lunar-tf2-msgs
BuildRequires:  ros-lunar-tf2-py
BuildRequires:  ros-lunar-xmlrpcpp

%description
This package contains the ROS bindings for the tf2 library, for both Python and
C++.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Jul 14 2017 Tully Foote <tfoote@osrfoundation.org> - 0.5.16-0
- Autogenerated by Bloom

* Thu Mar 30 2017 Tully Foote <tfoote@osrfoundation.org> - 0.5.15-0
- Autogenerated by Bloom

