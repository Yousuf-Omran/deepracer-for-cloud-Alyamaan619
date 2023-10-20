from math import exp

def reward_function(params):
    # Read input parameters
    left = params['is_left_of_center']
    wp = params['closest_waypoints'][1]
    
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    
    reward = 5*speed**5 + (2*exp(-0.2*steering_angle))
    zero_val = 3e-3
    
    if left == True:
        if wp in (list(range(67,99))):
           reward= zero_val

        else:
           reward *= 1.5

    else:
        if wp in (list(range(67,99))):
           reward *= 5

    #Always return a float value
    return float(reward)
