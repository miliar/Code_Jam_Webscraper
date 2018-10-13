#!/usr/bin/env python

import re
import os
import sys
import time
from copy import copy
from itertools import *
import os.path as path

try:
    import psyco
    psyco.full()
except:
    pass

def readint():
    return int(raw_input())

def readfloat():
    return float(raw_input())

def readlinearray(function):
    return map(function, raw_input().split())

def main():
    T = readint()
    for count in range(T):
        N = readint()
        points = []
        intersections = 0
        for n in range(N):
            a, b = readlinearray(int)
            points.append((a, b))
        for i, Pi in enumerate(points):
            for j in range(i, len(points)):
                Pj = points[j]
                if (Pi[0] > Pj[0] and Pi[1] < Pj[1] or \
                        Pi[0] < Pj[0] and Pi[1] > Pj[1]):
                    intersections += 1
        print 'Case #' + str(count + 1) + ':',
        print intersections

if __name__ == '__main__':
    main()

