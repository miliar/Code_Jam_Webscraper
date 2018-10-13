#!/usr/bin/env python
#
#
# "Bullseye", Round 1A
# Author:   Jon Makela
# Email:    socillion@gmail.com
# Google Code Jam 2013 Round 1A - Apr 26 2013

# Language: Python 2.7

import sys
import math
from math import pi
from pprint import pprint



DBG = True
FILE_LOC = "sample.txt"


def handleCase(r, t):
    """ r: first circle around white center of this radius
        t: start with this many ml of paint. Disk with radius of
        1cm = pi cm^2 = 1 ml paint used.
        Returns: max # of rings that maria can draw."""
    curr_radius = r
    paint_left = t
    ring_count = 0
    last_paint = ((curr_radius+1)**2) - (curr_radius**2)
    paint_for_next = last_paint-4
    while 1:
        paint_for_next += 4
        if paint_left < paint_for_next:
            return ring_count
        else:
            ring_count += 1
            paint_left -= paint_for_next
   # return ring_count

def totalRings(r,t):
    start_paint = (r+1)**2 - r**2
    total_paint = t
    n = math.sqrt(t)
    while 1:
        tmp = 0.5*n*(2*start_paint + (n-1)*4)
        if tmp <= t:
            return n
        else:
            n -= 1
    print "z: %s" % n
    return n
    # nth = start_paint + 4n

# 1st: 3 for 1st ring, 7 for 2nd
# sum: 0.5*n*(2a + (n-1)*d)
# d = increment, a = start
# S = 0.5n*(2a + (n-1)*4)
# a is known number, so is S

def readFile():
    "Uses FILE_LOC"
    with open(FILE_LOC) as fh:
        num_cases = int(fh.readline())
        data = []
        for i in xrange(num_cases):
            tmp = ""
            (r, t) = fh.readline().split()
            r = int(r)
            t = int(t)
            data.append(tuple((r,t)))
    return data

def printCase(str):
    print("Case #%d: %s" % (printCase.num,str))
    printCase.num += 1
printCase.num = 1

def printResult(res):
    printCase(str(res))

def main():
    if len(sys.argv) > 1:
        global FILE_LOC
        FILE_LOC = sys.argv[1]
    data = readFile()
    # data: list of tuples of (r,t)
    for r,t in data:
        printResult(handleCase(r, t))


if __name__ == '__main__':
    main()
