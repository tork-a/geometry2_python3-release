Name:           ros-kinetic-tf2-sensor-msgs
Version:        0.5.17
Release:        0%{?dist}
Summary:        ROS tf2_sensor_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-kinetic-python-orocos-kdl
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf2
Requires:       ros-kinetic-tf2-ros
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-catkin >= 0.5.6
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf2
BuildRequires:  ros-kinetic-tf2-ros

%description
Small lib to transform sensor_msgs with tf. Most notably, PointCloud2

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Jan 05 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.17-0
- Autogenerated by Bloom

* Sat Jul 15 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.16-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.15-0
- Autogenerated by Bloom

* Mon Jan 16 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.14-0
- Autogenerated by Bloom

* Thu Mar 31 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.13-0
- Autogenerated by Bloom

