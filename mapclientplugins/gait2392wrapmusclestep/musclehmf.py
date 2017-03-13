#testing the muscle hmf step

import gait2392MuscleCustomiser
from gias2.musculoskeletal import osim
import numpy as np

filename = 'gait2392_simbody.osim'

#load in the model
osimModel = osim.Model(filename)

config = {}
config['identifier'] = ''
config['osim_output_dir'] = './gait2392_simbody_custom.osim'
config['in_unit'] = 'mm'
config['out_unit'] = 'm'
config['write_osim_file'] = False
config['update_knee_splines'] = False
config['static_vas'] = False

ll = 


musclehmf = gait2392MuscleCustomiser(config, ll, osimModel):

