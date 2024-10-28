cmake_minimum_required(VERSION 3.5)
project(my_gazebo_robot)

# Check if using GCC or Clang and set compiler options
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find ament_cmake package
find_package(ament_cmake REQUIRED)

# Find other dependencies (uncomment and add dependencies if needed)
# find_package(<dependency> REQUIRED)

# Install launch and model directories
install(
    DIRECTORY launch model
    DESTINATION share/${PROJECT_NAME}
)

# Enable testing if requested
if(BUILD_TESTING)
    find_package(ament_lint_auto REQUIRED)

    # Uncomment the following line when a copyright and license are added to all source files
    set(ament_cmake_copyright_FOUND TRUE)

    # The following line skips cpplint (only works in a git repo)
    # Uncomment when this package is in a git repo and when
    # a copyright and license are added to all source files
    set(ament_cmake_cpplint_FOUND TRUE)

    ament_lint_auto_find_test_dependencies()
endif()

ament_package()

