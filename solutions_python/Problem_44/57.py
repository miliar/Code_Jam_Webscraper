from __future__ import with_statement, division
import sys
from decimal import Decimal
from math import sqrt

def dot(u, v):
    return sum(map(lambda a,b: a*b, u, v))

def cross(u, v):
    return u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]

def dist(x, y):
    return sqrt(sum(map(lambda a,b: (a-b)**2, x, y)))

def min_d(x1, x2):
    zero = (0, 0, 0)
    m = (x2[0]-x1[0], x2[1]-x1[1], x2[2]-x1[2])
    try:
        return dist(cross(m, x1), zero) / dist(x2, x1)
    except ZeroDivisionError:
        return dist(x1, zero)

def center(x):
    xbar = sum((xi[0] for xi in x)) / num_fireflies
    ybar = sum((xi[1] for xi in x)) / num_fireflies
    zbar = sum((xi[2] for xi in x)) / num_fireflies
    return xbar, ybar, zbar

with open(sys.argv[1]) as f:
    num_cases = int(f.readline())

    for c in xrange(1, num_cases+1):
        num_fireflies = int(f.readline())

        ffly = [map(Decimal, f.readline().split())
                for i in xrange(num_fireflies)]
        fx = [ff[:3] for ff in ffly]
        fx2 = [[x+ffly[i][3+j] for j, x in enumerate(ff)]
               for i, ff in enumerate(fx)]
        cx, cx2 = center(fx), center(fx2)
        diff = map(lambda a,b: a-b, cx2, cx)
        d = min_d(cx, cx2)
        try:
            t = -1 * float(dot(cx, diff)) / dist(cx2, cx)**2
        except ZeroDivisionError:
            t = 0.0
        if t < 0:
            t = 0.0
            d = dist(cx, (0,0,0))

        print "Case #%d: %.5f %.5f" % (c, d, t)
