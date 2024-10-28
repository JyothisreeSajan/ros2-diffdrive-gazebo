import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # This name has to match the robot name in the Xacro file
    robot_xacro_name = 'differential_drive_robot'
    
    # This is the name of our package, at the same time this is the name of the folder that will be used to define the paths
    package_name = 'my_gazebo_robot'
    
    # This is a relative path to the xacro file defining the model
    model_file_relative_path = 'model/robo.xacro'
    
    # This is a relative path to the Gazebo world file
    world_file_relative_path = 'model/empty_world.world'
    
    # This is the absolute path to the model
    path_model_file = os.path.join(get_package_share_directory(package_name), model_file_relative_path)
    
    # This is the absolute path to the world model
    path_world_file = os.path.join(get_package_share_directory(package_name), world_file_relative_path)
    
    # Get the robot description from the xacro model file
    robot_description = xacro.process_file(path_model_file).toxml()
    
    # Gazebo ROS package launch
    gazebo_ros_package_launch = PythonLaunchDescriptionSource(
        os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
    )
    
    # This is the launch description for Gazebo
    gazebo_launch = IncludeLaunchDescription(
        gazebo_ros_package_launch,
        launch_arguments={'world': path_world_file}.items()
    )
    
    # Here, we create a gazebo_ros Node to spawn the model
    spawn_model_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', robot_xacro_name],
        output='screen'
    )
    
    # Robot State Publisher Node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description, 'use_sim_time': True}]
    )
    
    # Create the launch description object
    launch_description_object = LaunchDescription()
    
    # Add gazebo_launch
    launch_description_object.add_action(gazebo_launch)
    
    # Add the two nodes
    launch_description_object.add_action(spawn_model_node)
    launch_description_object.add_action(node_robot_state_publisher)
    
    return launch_description_object  # Ensure this is on its own line

