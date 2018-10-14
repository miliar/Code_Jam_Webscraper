'''
Created on May 8, 2010

@author: jmvieira
'''

from collections import deque
import sys

f_in = open(sys.argv[1], 'r')
f_out = open(sys.argv[2], 'w')

T = int(f_in.readline())

for case_n in range(1, T + 1):
    test_pars = f_in.readline().split()
    n_rides = int(test_pars[0])
    ride_capacity = int(test_pars[1])
    
    queue = deque(f_in.readline().split())
    new_queue = queue.__copy__()
    euros = 0
    
    for ride in range(1, n_rides + 1):
        max = ride_capacity
        
        for group in queue:
            max -= int(group)
            
            if max >= 0:
                euros += int(group)
                new_queue.append(new_queue.popleft()) 
            else:
                queue = new_queue.__copy__()
                break
    
    f_out.write('Case #%d: %d\n' % (case_n, euros))