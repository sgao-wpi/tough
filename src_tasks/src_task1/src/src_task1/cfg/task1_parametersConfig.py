## *********************************************************
## 
## File autogenerated for the src_task1 package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'PANELWALKPOSE', 'lower': 'panelwalkpose', 'srcline': 121, 'name': 'panelWalkPose', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::PANELWALKPOSE', 'field': 'DEFAULT::panelwalkpose', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 14, 'description': 'x of goal location', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'x_pw', 'edit_method': '', 'default': 2.828, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 15, 'description': 'y of goal location', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_pw', 'edit_method': '', 'default': 0.292, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 16, 'description': 'theta of goal location', 'max': 1.57, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'theta_pw', 'edit_method': '', 'default': 0.82, 'level': 0, 'min': -1.57, 'type': 'double'}], 'type': '', 'id': 1}, {'upper': 'PANELFINALPOSE', 'lower': 'panelfinalpose', 'srcline': 121, 'name': 'panelFinalPose', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::PANELFINALPOSE', 'field': 'DEFAULT::panelfinalpose', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 20, 'description': 'x of goal location', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'x_pf', 'edit_method': '', 'default': 2.828, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 21, 'description': 'y of goal location', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_pf', 'edit_method': '', 'default': 0.292, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 22, 'description': 'theta of goal location', 'max': 1.57, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'theta_pf', 'edit_method': '', 'default': 0.82, 'level': 0, 'min': -1.57, 'type': 'double'}], 'type': '', 'id': 2}, {'upper': 'FINISHBOXWALKPOSE', 'lower': 'finishboxwalkpose', 'srcline': 121, 'name': 'finishBoxWalkPose', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::FINISHBOXWALKPOSE', 'field': 'DEFAULT::finishboxwalkpose', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 26, 'description': 'x of goal location', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'x_fb', 'edit_method': '', 'default': 2.828, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 27, 'description': 'y of goal location', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_fb', 'edit_method': '', 'default': 0.292, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 28, 'description': 'theta of goal location', 'max': 1.57, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'theta_fb', 'edit_method': '', 'default': 0.82, 'level': 0, 'min': -1.57, 'type': 'double'}], 'type': '', 'id': 3}, {'upper': 'HANDLELOC', 'lower': 'handleloc', 'srcline': 121, 'name': 'handleLoc', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::HANDLELOC', 'field': 'DEFAULT::handleloc', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 32, 'description': 'x of pitch knob center', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'p_c_x', 'edit_method': '', 'default': 2.828, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 33, 'description': 'y of pitch knob center', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'p_c_y', 'edit_method': '', 'default': 0.292, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 34, 'description': 'z of pitch knob center', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'p_c_z', 'edit_method': '', 'default': 0.89, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 36, 'description': 'x of pitch knob handle', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'p_h_x', 'edit_method': '', 'default': 2.828, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 37, 'description': 'y of pitch knob handle', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'p_h_y', 'edit_method': '', 'default': 0.292, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 38, 'description': 'z of pitch knob handle', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'p_h_z', 'edit_method': '', 'default': 0.89, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 40, 'description': 'x of yaw knob center', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_c_x', 'edit_method': '', 'default': 2.828, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 41, 'description': 'y of yaw knob center', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_c_y', 'edit_method': '', 'default': 0.292, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 42, 'description': 'z of yaw knob center', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_c_z', 'edit_method': '', 'default': 0.89, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 44, 'description': 'x of yaw knob handle', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_h_x', 'edit_method': '', 'default': 2.828, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 45, 'description': 'y of yaw knob handle', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_h_y', 'edit_method': '', 'default': 0.292, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 46, 'description': 'z of yaw knob handle', 'max': 1.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/ninja/indigo_ws/src/space_robotics_challenge/src_tasks/src_task1/cfg/task1_parameters.cfg', 'name': 'y_h_z', 'edit_method': '', 'default': 0.89, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 4}], 'parameters': [], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

