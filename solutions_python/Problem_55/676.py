#!/usr/bin/env python
from collections import deque

def earning(r, k, n, g_size):
    earned = 0
    queue = deque(g_size)
    
    for ride in xrange(r):
        groups_to_ride,people_to_ride = how_many_ride(k, queue)
        earned += people_to_ride
        
        for i in xrange(groups_to_ride):
            queue.append(queue.popleft())
    
    return earned    
        
def how_many_ride(k, queue):
    on_rc = 0
    grps_on_rc = 0    
    while len(queue) > grps_on_rc and queue[grps_on_rc] + on_rc <= k:
        on_rc += queue[grps_on_rc]
        grps_on_rc += 1        
    return grps_on_rc, on_rc
        
if __name__ == "__main__":
    with open("/tmp/input", "r") as f:
        with open("/tmp/output", "w+") as g:
            t = int(f.readline())
            for i in xrange(t):
                ints = [int(s) for s in f.readline().split()]
                sizes = [int(s) for s in f.readline().split()]
                g.write("Case #" + str(i + 1) + ": " + str(earning(ints[0], ints[1], ints[2], sizes)) + "\n")
