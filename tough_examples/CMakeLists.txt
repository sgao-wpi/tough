cmake_minimum_required(VERSION 2.8.3)
project(tough_examples)

add_definitions(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  tough_controller_interface
  tough_common
  tough_footstep
  tough_perception_common
  tough_moveit_planners
)


catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES tough_examples
  CATKIN_DEPENDS 	roscpp
                        rospy
                        std_msgs
                        tough_controller_interface
                        tough_common
                        tough_footstep
                        tough_perception_common
                        tough_moveit_planners
#  DEPENDS system_lib
)


###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)

######################
## Control examples ##
######################


## Reset Robot
add_executable( reset_robot src/control_examples/reset_robot.cpp)
add_dependencies(reset_robot ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(reset_robot ${catkin_LIBRARIES})


## Test ARM
add_executable( arm_control_example src/control_examples/arm_control_example.cpp)
add_dependencies(arm_control_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(arm_control_example ${catkin_LIBRARIES})


## Test head navigation
add_executable( head_control_example src/control_examples/head_control_example.cpp)
add_dependencies(head_control_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(head_control_example ${catkin_LIBRARIES})

## Test arm navigation
add_executable(arm_control_example2 src/control_examples/arm_control_example2.cpp)
add_dependencies(arm_control_example2 ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(arm_control_example2  ${catkin_LIBRARIES})

## Test chest
add_executable(chest_control_example src/control_examples/chest_control_example.cpp)
add_dependencies(chest_control_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(chest_control_example  ${catkin_LIBRARIES})


## Test nudgeLocal
add_executable(nudge_local_example src/control_examples/nudge_local_example.cpp)
add_dependencies(nudge_local_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(nudge_local_example  ${catkin_LIBRARIES})


## Test pelvis
add_executable(pelvis_control_example src/control_examples/pelvis_control_example.cpp)
add_dependencies(pelvis_control_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(pelvis_control_example  ${catkin_LIBRARIES})


## Test neck
add_executable(neck_control_example src/control_examples/neck_control_example.cpp)
add_dependencies(neck_control_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(neck_control_example  ${catkin_LIBRARIES})

## Test gripper
add_executable(gripper_control_example src/control_examples/gripper_control_example.cpp)
add_dependencies(gripper_control_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(gripper_control_example  ${catkin_LIBRARIES})


## interactive test
add_executable(arm_interactive_example src/control_examples/arm_interactive_example.cpp)
add_dependencies(arm_interactive_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(arm_interactive_example  ${catkin_LIBRARIES})

# ## nudge offset
# add_executable(nudge_offset_example src/control_examples/nudge_offset_example.cpp)
# add_dependencies(nudge_offset_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
# target_link_libraries(nudge_offset_example  ${catkin_LIBRARIES})


#########################
## Navigation examples ##
#########################

add_executable(walk_forward_example src/navigation_examples/walk_forward_example.cpp )
add_dependencies(walk_forward_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(walk_forward_example  ${catkin_LIBRARIES})

add_executable(walk_goal_example src/navigation_examples/walk_goal_example.cpp )
add_dependencies(walk_goal_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(walk_goal_example  ${catkin_LIBRARIES})

add_executable(walk_example src/navigation_examples/walk_example.cpp )
add_dependencies(walk_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(walk_example  ${catkin_LIBRARIES})

add_executable(walk_rotate_example src/navigation_examples/walk_rotate_example.cpp )
add_dependencies(walk_rotate_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(walk_rotate_example  ${catkin_LIBRARIES})

add_executable(walk_steps_example src/navigation_examples/walk_steps_example.cpp )
add_dependencies(walk_steps_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(walk_steps_example  ${catkin_LIBRARIES})


#########################
## Perception examples ##
#########################
add_executable(multisense_image_example src/perception_examples/test_multisense_image.cpp )
add_dependencies(multisense_image_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(multisense_image_example  ${catkin_LIBRARIES})

#########################
## Manipulation examples ##
#########################

add_executable(ik_example src/manipulation_examples/ik_example.cpp )
add_dependencies(ik_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ik_example  ${catkin_LIBRARIES})

add_executable(motion_planner_example src/manipulation_examples/motion_planner_example.cpp )
add_dependencies(motion_planner_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(motion_planner_example  ${catkin_LIBRARIES})


add_executable(taskspace_planner_example src/manipulation_examples/taskspace_planner_example.cpp )
add_dependencies(taskspace_planner_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(taskspace_planner_example  ${catkin_LIBRARIES})

add_executable(taskspace_planner_interactive_example src/manipulation_examples/taskspace_planner_interactive_example.cpp )
add_dependencies(taskspace_planner_interactive_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(taskspace_planner_interactive_example  ${catkin_LIBRARIES})

add_executable(taskspace_2stage_planner_example src/manipulation_examples/taskspace_2stage_planner_example.cpp )
add_dependencies(taskspace_2stage_planner_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(taskspace_2stage_planner_example  ${catkin_LIBRARIES})

add_executable(follow_cartesian_path src/manipulation_examples/follow_cartesian_path.cpp )
add_dependencies(follow_cartesian_path ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(follow_cartesian_path  ${catkin_LIBRARIES})


install(TARGETS reset_robot arm_control_example head_control_example arm_control_example2
                chest_control_example nudge_local_example pelvis_control_example
                neck_control_example gripper_control_example arm_interactive_example
                walk_forward_example walk_goal_example walk_example walk_rotate_example walk_steps_example
                multisense_image_example ik_example motion_planner_example taskspace_planner_example 
                taskspace_2stage_planner_example taskspace_planner_interactive_example follow_cartesian_path
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

