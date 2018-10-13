#!/usr/bin/env python

import math
import sys

def indef_integral(x1, x0, r0):
    def f(x):
        return (x/2.0) * math.sqrt(r0*r0-x*x) + r0*r0*math.asin(x/r0)/2.0
    return f(x1) - f(x0)

def square_arc_intersect_area(c_x, c_y, d, r):

    # does the bottom-left of the square lie outside the arc?
    if c_x * c_x + c_y * c_y >= r*r:
        return 0

    # (c_x, c_y) is the bottom-left corner of the square of size d
    # r is the radius of the circle centered at the origin
    if (c_x+d) * (c_x+d) + (c_y+d) * (c_y+d) <= r*r:
        return d*d

    # where does the arc cross the right edge?

    left_rectangle_end = c_x

    left_edge_y_squared = r*r-c_x*c_x
    # case: arc intersects left edge of square
    if left_edge_y_squared > (c_y+d) * (c_y+d):
        # nope
        # where does the arc cross the top edge?
        left_rectangle_end = math.sqrt(r*r-(c_y+d)*(c_y+d))

    integral_x1 = c_x+d
    # case: arc intersects bottom
    # where does the arc cross the bottom edge?
    bottom_edge_x_squared = r*r-c_y*c_y
    if bottom_edge_x_squared < (c_x+d) * (c_x+d):
        integral_x1 = math.sqrt(bottom_edge_x_squared)

    return d * (left_rectangle_end-c_x) + indef_integral(integral_x1, left_rectangle_end, r) + c_y * (left_rectangle_end - integral_x1)

def do_trial(f, R, t, r, g):

    inner_radius = R-t

    total_fly_area = math.pi * R * R / 4.0

    fly_safe_area = 0.0

    s_x = r
    while s_x<inner_radius:
        s_y = r
        while s_y < inner_radius:
            fly_safe_area += square_arc_intersect_area(s_x+f, s_y+f, g-f-f, R-t-f)
            s_y += g+2*r
        s_x += g+2*r
    return 1.0-fly_safe_area/total_fly_area

f = sys.stdin
count = int(f.readline())
for i in xrange(count):
    args = [float(x) for x in f.readline().split()]
    #print args
    p = do_trial(*args)
    print "Case #%d: %1.6f" % (i+1, p)
