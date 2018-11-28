'''
Created on Apr 12, 2014

@author: fuellerm
'''

import sys

fil = open(sys.argv[1], 'r')
n = int(fil.readline())
for i in range(1, n+1):
    # read c, f and x from file
    strs = fil.readline().rstrip('\n').split(' ')
    [c, f, x] = [float(numeric_string) for numeric_string in strs]
    
    # calculate result in a loop iteratively
    prod = 2.0      # current cookie production
    time = 0.0      # current time
    cookies = 0.0   # current amount of cookies
    while cookies < x:
        
        # Calculate two options: 
        #   time needed to collect cookies if we are just lazy and dont do anything 
        #   time needed to collect cookies if we save cookies and buy a farm
        # Then decide with takes less time...if we opt for a farm, we advance to the point
        # in time when we buy the farm and continue with next iteration
        time_lazy = time + x / prod  # time to win without buying a farm
        time_farm = time + c / prod + x / (prod + f)
        if time_lazy < time_farm:
            time = time_lazy
            cookies = x
        else:
            time += c / prod
            prod += f
        
    print "Case #" + str(i) + ": " + str(round(time, 7))