#!/usr/bin/env python

from __future__ import division
from decimal import *
import math
import string

getcontext().prec = 1000
PI = Decimal(math.pi)

def circle_area(radius=1):
    return math.pi * radius * radius

def ring_area(radius=1, thickness=1):
    """ returns the area covered by a black ring
    of thickness 1, with the inner radius at 1 """
    inner = radius
    outer = radius + thickness
    return circle_area(radius=outer) - circle_area(radius=inner)

def paint_required(radius=1, thickness=1):
    """ paint required to draw a ring """
    return ring_area(radius=radius, thickness=thickness) / math.pi

def paint_required_inline(radius=1, thickness=1):
    outer = radius + thickness
    x = ((PI * outer * outer) - (PI * radius * radius)) / PI
    # print(radius, x)
    return x

def max_rings(radius=1, paint=1):
    """ calculate max rings """
    rings = 0
    # first ring
    required = paint_required_inline(radius=radius, thickness=1)
    while paint >= required:
        paint -= required
        rings += 1
        # next round
        radius += Decimal(2) # +1 to the outer black, +1 to next outer white
        required = paint_required_inline(radius=radius, thickness=1)
        # print(rings, paint, radius, required)
        
    return rings

if __name__ == '__main__':
    with open('A-small-attempt0.in') as handle:
        _ = handle.readline()
        for i, line in enumerate(handle, start=1):
            radius, paint = map(Decimal, map(string.strip, line.split()))
            print('Case #%s: %s' % (i, max_rings(radius=radius, paint=paint)))
