from sys import stdin
import numpy as np


num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    d,n = map(int, stdin.readline().strip().split(' '))

    tmax = 0.0
    for i in xrange(0,n):
        x0,v = map(int, stdin.readline().strip().split(' '))
        t = float(d - x0)/v
        tmax = max(tmax, t)
    vmax = d / tmax 

    print "Case #" + str(case_index) + ": " + str(vmax)
