#!/usr/bin/python

import sys;
import os.path; 
from collections import *;
from Queue import *;
import numpy as np;
import math

def readi():
    return int(sys.stdin.readline().strip());

def readia():
    return [int(x) for x in sys.stdin.readline().strip().split()];

def readfa():
    return [float(x) for x in sys.stdin.readline().strip().split()];

def reads():
    return sys.ggstdin.readline().strip();

def main():
    nt = readi();
    for t in range(1, nt+1):
        (N, K) = readia()
        rh = []
        for i in range(N):
            (R, H) = readia()
            rh.append((R, H, 2 * R * H, R * R))

        rh.sort(cmp=lambda x, y: -cmp(x[2], y[2]))
        # print rh


        if K > 1:
            maxR = max(x[0] for x in rh[:K-1])
            sumSide = sum(x[2] for x in rh[:K-1])
        else:
            maxR = 0
            sumSide = 0

        area = maxR * maxR + sumSide

        # print "maxR: ", maxR, "sumside ", sumSide

        bestArea = 0
        for i in range(K-1, N):
            (r, h, side, top) = rh[i]
            deltaR = max(r - maxR, 0)
            deltaSq = max(r * r - maxR * maxR, 0) + side
            # print "i = ", i, ", deltaSq = ", deltaSq
            if deltaSq > bestArea:
                bestArea = deltaSq

        # print bestArea
        res = area + bestArea
        print "Case #%d: %0.9f" % (t, math.pi * res);
    

main();
