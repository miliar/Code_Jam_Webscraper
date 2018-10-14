#!/usr/bin/env python

import math
import operator
import re
import sys

line = sys.stdin.readline()
line = line.rstrip()

cases = int(line)

def close(a,b):
    diff = a-b
    return -0.000001 < diff and diff < 0.000001

def inside(x,y,r):
    return x*x+y*y < r*r

def opposite(a,r):
    return math.sqrt(r*r-a*a)

def segmentarea(h, r):
    return (r*r*math.acos(h/r) - h*opposite(h,r))
    
# this is the area of a piece of the circle between two chords h1 and
# h2 from the center (where h1 > h2), between a line perpendicular to
# the chords d from the center and the edge.
def piece(h1, h2, d, r):
    s1 = segmentarea(h1, r)
    s2 = segmentarea(h2, r)
    halfslice = (s1-s2)/2
    a = halfslice-((h2-h1)*d)
    return a

for case in range(0, cases):
    (f,R,t,r,g) = map(float, sys.stdin.readline().rstrip().split())

    # adjust the parameters for a size zero fly

    t = t + f
    r = r + f
    g = g - 2*f
    f = 0

    # inner radius of ring is useful
    IR = R-t

    A = 0.0

    y = 0
    while y <= R:
        x = 0
        while x <= R:
            if close(x,y):
                mult = 0.5
            elif x < y:
                mult = 1
            else:
                x += 2*r+g
                continue

            holeleft = x+r
            holeright = holeleft+g
            holelower = y+r
            holeupper = holelower+g

            llinside = inside(holeleft, holelower, IR)
            lrinside = inside(holeright, holelower, IR)
            ulinside = inside(holeleft, holeupper, IR)
            urinside = inside(holeright, holeupper, IR)

            if urinside:
                area = g*g
            elif ulinside:
                ixupper = opposite(holeupper, IR)
                area = (ixupper-holeleft)*g+\
                       piece(ixupper, holeright, holelower, IR)
            elif lrinside:
                area = piece(holeleft, holeright, holelower, IR)
            elif llinside:
                ixlower = opposite(holelower, IR)
                area = piece(holeleft, ixlower, holelower, IR)
            else:
                break

            A += area*mult
            x += 2*r+g
        y += 2*r+g

    A *= 8

    CA = math.pi*R*R
    pmissfly = A/CA
    phitfly = 1-pmissfly

    print "Case #%d: %0.6f" % (case+1, phitfly)
