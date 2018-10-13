#! /usr/bin/env python

from sys import stdin
import sys

def mintime(r, c, f, x):
    m = 0.
    while (c / r) + (x / (r + f)) < x / r:
        m += c / r
        r += f
    m += x / r
    return m

ntest = input()

for test in xrange(ntest):
    c, f, x = [float(i) for i in stdin.readline().strip().split(' ')]
    print "Case #{}: {:.7f}".format(test+1, mintime(2., c, f, x))