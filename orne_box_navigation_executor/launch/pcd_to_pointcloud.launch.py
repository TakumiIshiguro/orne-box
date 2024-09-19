import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():    
    return LaunchDescription([
        Node(
            package='pcl_ros',
            executable='pcd_to_pointcloud',
            name='pcd_to_pointcloud',
            output='screen',
            parameters=[{
                'file_name': '/home/ros2_ws/src/orne-box/orne_box_navigation_executor/config/maps/3F_map.pcd',
                'tf_frame': 'map'
            }],
            remappings=[
                ('/cloud_pcd', '/map')
            ]
        ),
    ])
