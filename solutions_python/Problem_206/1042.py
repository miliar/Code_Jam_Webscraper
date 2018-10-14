from __future__ import print_function
import sys
import numpy as np
import math

filename = 'A-small-attempt0.in'
#filename = 'cruisesample'

def getspeed(D, plist):
    maxtime = 0
    for a in plist:
        if maxtime == 0:
            maxtime = (D - a[0]) / a[1]
        else:
            maxtime = max(maxtime, (D - a[0]) / a[1])
    return D / maxtime

#Read data
if len(sys.argv) < 2:
    print("Missing input file name")
    quit()
with open(sys.argv[1], "r") as f:
#with open(filename, "r") as f:
    T = int(f.readline())
    for x in range(T):
        plist = []
        D, N = [int(z) for z in f.readline().split()]
        for y in range(N):
            plist.append([int(z) for z in f.readline().split()])
        print("Case #%d: %f" % (x + 1, getspeed(D, plist)))
