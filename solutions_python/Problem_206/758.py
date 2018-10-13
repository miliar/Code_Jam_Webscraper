# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
from __future__ import division

def solve(dist, states):
    max_hrs = 0
    for state in states:
        position, speed = state
        current_hrs = (dist - position)/speed
        if current_hrs > max_hrs:
            max_hrs = current_hrs
    return dist/max_hrs

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    total_dist, horses = [int(s) for s in raw_input().split(" ")]
    init_states = []
    for horse in xrange(horses):
        position, speed = [int(s) for s in raw_input().split(" ")]
        init_states.append((position,speed))
    result = solve(total_dist, init_states)
    print "Case #{0}: {1:.6f}".format(i,result)
    # check out .format's specification for more formatting options