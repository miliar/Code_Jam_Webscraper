import sys
import math

def solve(d, horses):
    slow_hour_max = 0
    for h in horses:
        slow_hour = float(d - h[0])/float(h[1])
        if slow_hour_max < slow_hour:
            slow_hour_max = slow_hour

    return d / slow_hour_max

t = int(raw_input())
for i in xrange(1, t + 1):
    arg1 = raw_input().split(" ")
    d = int(arg1[0])
    n = int(arg1[1])

    horses = []
    for j in range(n):
        arg2 = raw_input().split(" ")
        k = int(arg2[0])
        s = int(arg2[1])

        horses.append([k, s])

        solution = solve(d, horses)

    print "Case #%d: %.6f" % (i, solution)
    

        
        
        
        
        
