#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from __future__ import with_statement

from optparse import OptionParser
import sys
import re
import math

parser = OptionParser()
parser.add_option("-d", "--debug", action="store_true", dest="debug")

pi = math.pi
squares = 0

(options, args) = parser.parse_args()

def decorator(old_decorator):
    "Restore original name, doc & dict for decorated functions"
    def new_decorator(f):
        g = old_decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g

    new_decorator.__name__ = old_decorator.__name__
    new_decorator.__doc__ = old_decorator.__doc__
    new_decorator.__dict__.update(old_decorator.__dict__)

    return new_decorator

def memoize(cache=None):
    """Decorator to memoize a function
    Can be used on multiple functions
    Warning: Does not reclaim memory"""

    if cache == None:
        cache = {}

    @decorator
    def m(f):
        def g(*args, **kwargs):
            key = ( f, tuple(args), frozenset(kwargs.items()) )
            if key not in cache:
                cache[key] = f(*args, **kwargs)
            return cache[key]

        return g

    return m

def overlap(r, x, mx, y, my, min_area):
    #assert r >= 0.0
    #assert mx >= x, '%s >= %s' % (mx, x)
    #assert my >= y, '%s >= %s' % (my, y)

    max_area = (mx - x) * (my - y)
    topright = math.hypot(mx, my)
    bottomleft = math.hypot(x, y)
    #print 'overlap', squares, int(100.0 * max_area / min_area)
    if r >= topright:
        # Square entirely inside
        #print 'max'
        return max_area
    elif r <= bottomleft:
        # Square entirely outside
        #print 'zero'
        return 0.0
    elif max_area > min_area:
        # Split the region into 4 parts
        midx = (mx + x) / 2.0
        midy = (my + y) / 2.0
        area = overlap(r, x,    midx, y,    midy, min_area) + \
               overlap(r, midx, mx,   midy, my,   min_area) + \
               overlap(r, midx, mx,   y,    midy, min_area) + \
               overlap(r, x,    midx, midy, my,   min_area)
        return area
    else:
        # Guesstimate area from circle intercept points
        #print 'guess %0.6f' %  (max_area * (r - bottomleft) / (topright - bottomleft))
        return max_area * (r - bottomleft) / (topright - bottomleft)


#testcases = [(1.0, 0.0, 2.0, 0.0, 2.0, pi / 4.0)]
#for tc in testcases:
#    print overlap(tc[0], tc[1], tc[2], tc[3], tc[4], tc[0] / 100000000.0), '=', tc[5]
#    assert abs(tc[5] - overlap(tc[0], tc[1], tc[2], tc[3], tc[4], tc[0] / 100000000.0)) < 0.00001

if args:
    input_filename = args[0]

    file = open(input_filename, 'r')

    num_tests = int(file.readline().strip())
    if options.debug:
        print "num_tests", num_tests

    for test in range(1, num_tests + 1):
        match = re.search(r'^([0-9\.]+)\s([0-9\.]+)\s([0-9\.]+)\s([0-9\.]+)\s([0-9\.]+)\s*$', file.readline().strip())
        assert match, 'Bad input'

        f = float(match.group(1))
        R = float(match.group(2))
        t = float(match.group(3))
        r = float(match.group(4))
        g = float(match.group(5))

        squares = 0

        if options.debug:
            print "Test %s %0.6f %0.6f %0.6f %0.6f %0.6f" % (test, f, R, t, r, g)

        # We consider only 1/4 segment of racket (it is symmetrical)
        total_area = (pi * R * R) / 4.0
        stringR = R - t - f
        if stringR < 0.0:
            stringR = 0.0
        hit_area = total_area - ((pi * stringR * stringR) / 4.0)

        if options.debug:
            print "total_area: %0.6f\nhit_area: %0.6f" % (total_area, hit_area)

        xpos = 0.0 + r + f
        ypos = 0.0 + r + f
        miss_area = 0.0
        error_bounds = total_area / 10000000.0 # Ensure 6 digit accuracy
        if options.debug:
            print 'ypos', ypos
            print 'stringR', stringR
        while ypos < stringR:
            # calculate area of square inside racquet
            xmax = xpos + g - f - f
            ymax = ypos + g - f - f
            squares += 1
            miss = overlap(stringR, xpos, xmax, ypos, ymax, error_bounds)
            if options.debug:
                print test, squares
            miss_area += miss
            if miss == 0.0:
                xpos = 0.0 + r + f # back to beginning of line
                ypos += g + r + r # up a line (string width + hole width)
            else:
                xpos += g + r + r

        if options.debug:
            print 'miss_area = %0.6f' % miss_area
            print 'Possible', (pi * stringR * stringR) / 4.0

        print "Case #%s: %0.6f" % (test, 1.0 - (miss_area / total_area))
