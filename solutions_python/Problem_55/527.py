import sys
import math

fname = "C-small-attempt0"
debug = False
inp = open(fname + ".in", "r")
out = None
if debug:
    out = sys.stdout
else:
    out = open(fname + ".out", "w")
num_cases = int(inp.readline())
for i in xrange(num_cases):
    out.write("Case #%d: " % (i+1))
    times, at_once, ngroups = inp.readline().strip().split(' ')
    at_once = int(at_once)
    ngroups = int(ngroups)
    queue = inp.readline().strip().split(' ')
    euros = 0
    for k in xrange(int(times)):
        p_ride = 0
        for j in xrange(ngroups):
            people = int(queue[0]) + p_ride
            if people <= at_once:
                queue = queue[1:] + [queue[0]]
                p_ride = people
            else:
                break
        euros += p_ride
    out.write(str(euros) + '\n')
