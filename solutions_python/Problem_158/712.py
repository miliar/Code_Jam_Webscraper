#!/usr/bin/env python

import sys

from copy import copy
from array import array
from math import ceil, sqrt
from pprint import pprint

class A(object):
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.a = array('c', ['o'] * (self.r * self.c))

    def printa(self):
        for y in xrange(self.r):
            for x in xrange(self.c):
                print self.a[y * self.c + x],
            print
        print

    def hole_sizes(self, r=0, c=0):
        res = []
        for y in xrange(self.r):
            for x in xrange(self.c):
                if self.a[y * self.c + x] in ('x', '.'):
                    continue
                hole_size = self.fill(x, y)
                res.append(hole_size)
                #print "hole size", hole_size
                #self.printa()
        return res

    def fill(self, x, y, s=0):
        self.a[y * self.c + x] = '.'
        ns = s + 1
        for dx in (1, -1):
            if x + dx >= 0 and x + dx < self.c and self.a[y * self.c + x + dx] == 'o':
                ns = self.fill(x + dx, y, ns)
        for dy in (1, -1):
            if y + dy >= 0 and y + dy < self.r and self.a[(y + dy) * self.c + x] == 'o':
                ns = self.fill(x, y + dy, ns)
        return ns

    def __setitem__(self, x, i):
        self.a[x[1] * self.c + x[0]] = i

def place(omino, R, C):
    placements = []
    for variant in [        h_mirrored(omino),         v_mirrored(omino),         rotated(omino),         rotated(rotated(omino)),         rotated(rotated(rotated(omino))),        omino    ]:
        for r in xrange(R):
            for c in xrange(C):
                a = A(R, C)
                for e in variant:
                    if e[0] + c < C and e[1] + r < R:
                        a[(e[0] + c, e[1] + r)] = 'x'
                    else:
                        break
                else:
                    #print "PLACING", R, C, r, c, variant
                    #a.printa()
                    placements.append(a)

    return placements
          
def solve(X, R, C):
    if X >= 7:
        return "RICHARD"
    elif X == 1:
#        print "lucky one criterium"
        return "GABRIEL"
    else:
        if (R * C) % X != 0: # or min(R, C) < min(X / 2, int(ceil(X / 2.0))) and max(R, C) < max(X / 2, int(ceil(X / 2.0))):
#            print "mod criterium"
            return "RICHARD"
        else:
            ominos = minorator(X)
            for omino in ominos:
                placements = place(omino, R, C)
                if not placements:
#                    print "omino too large criterium"
                    return "RICHARD"
                else:
                    hole_sizes = [hole_size for placement in placements for hole_size in placement.hole_sizes()]
                    if hole_sizes and all(hole_size < X for hole_size in hole_sizes):
#                        print "hole criterium"
                        #for placement in placements:
                        #    placement.printa()
                        return "RICHARD"
                    else:
                        pass
                        #for placement in placements:
                        #    placement.printa()

#            print "all ok criterium"
            return "GABRIEL"

def h_mirrored(no):
    res = []
    for e in no:
        res.append((-e[0], e[1]))

    while(any(x < 0 for x, y in res)):
        for i, r in enumerate(res):
            res[i] = (r[0] + 1, r[1])

    while(any(y < 0 for x, y in res)):
        for i, r in enumerate(res):
            res[i] = (r[0], r[1] + 1)

    return tuple(sorted(res))

def v_mirrored(no):
    res = []
    for e in no:
        res.append((e[0], -e[1]))

    while(any(x < 0 for x, y in res)):
        for i, r in enumerate(res):
            res[i] = (r[0] + 1, r[1])

    while(any(y < 0 for x, y in res)):
        for i, r in enumerate(res):
            res[i] = (r[0], r[1] + 1)

    return tuple(sorted(res))

def rotated(no):
    res = []
    for e in no:
        res.append((-e[1], e[0]))

    while(any(x < 0 for x, y in res)):
        for i, r in enumerate(res):
            res[i] = (r[0] + 1, r[1])

    while(any(y < 0 for x, y in res)):
        for i, r in enumerate(res):
            res[i] = (r[0], r[1] + 1)

    return tuple(sorted(res))

x = ((0, 0), (0, 1), (1, 0))
#print x
#print rotated(x)
#print rotated(rotated(x))
#print rotated(rotated(rotated(x)))
#print rotated(rotated(rotated(rotated(x))))

def minorator(t):
    if t == 1:
        return [[ (0, 0), ]]
    else:
        res = []
        t1s = minorator(t - 1)
        for t1 in t1s:
            for e in t1:
                for d in [(1, 0), (0, 1)]:
                    ne = (e[0] + d[0], e[1] + d[1])
                    if ne not in t1:
                        nt = tuple(sorted(list(t1) + [ne]))
                        if nt not in res and h_mirrored(nt) not in res and v_mirrored(nt) not in res and rotated(nt) not in res and rotated(rotated(nt)) not in res and rotated(rotated(rotated(nt))) not in res:
                            res.append(nt)
        return res

if __name__ == '__main__':
    input_file = open(sys.argv[1])
    T = int(input_file.readline().strip())
    first_test_case = 1

    for x in xrange(T):
        X, R, C = [int(p) for p in input_file.readline().strip().split()]
        if R > C:
            R, C = C, R

#        print X, R, C
        print "Case #{case}: {winner}".format(
            case=(x + first_test_case),
            winner=solve(X, R, C)
        )

