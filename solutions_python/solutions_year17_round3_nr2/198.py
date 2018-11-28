from __future__ import print_function
import sys
import numpy as np
import math

def getans(C, J, clist, jlist):
    if C == 2:
        if (clist[0][1] - clist[1][0])%(24*60)<=12*60 or (clist[1][1] - clist[0][0])%(24*60)<=12*60:
            return 2
        return 4
    if J == 2:
        if (jlist[0][1] - jlist[1][0])%(24*60)<=12*60 or (jlist[1][1] - jlist[0][0])%(24*60)<=12*60:
            return 2
        return 4
    return 2

#Read data
if len(sys.argv) < 2:
    print("Missing input file name")
    quit()
with open(sys.argv[1], "r") as f:
    T = int(f.readline())
    for x in range(T):
        clist = []
        jlist = []
        C, J = [int(z) for z in f.readline().split()]
        for y in range(C):
            clist.append([int(z) for z in f.readline().split()])
        for y in range(J):
            jlist.append([int(z) for z in f.readline().split()])
        print("Case #%d: %d" % (x + 1, getans(C, J, clist, jlist)))
