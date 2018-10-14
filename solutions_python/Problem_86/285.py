#!/usr/bin/python2.7
#
# Code Jam 2011
# 21 May 2011 - Round 1C
#
# C - Perfect Harmony
#
#
##Input
##
##2
##3 2 100
##3 5 7
##4 8 16
##1 20 5 2
##
##Output 
##
##Case #1: NO
##Case #2: 10
#

from __future__ import division
from itertools import tee, izip, islice, combinations

import sys


inp, out = sys.stdin, sys.stdout

def logit(case, output):
    out.flush()
    out.write("Case #%d: %s\n" %(case, output))
    out.flush()

    
def lcm(numbers):
    return reduce(__lcm, numbers)


def __lcm(a, b):
    return ( a * b ) / __gcd(a, b)


def __gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def divides(freqs, n):
    ds = []
    
def test():
    T = int(inp.readline())
    i1, i2 = tee(inp, 2)
    for case, nlh, line in izip(xrange(1, T+1),
                              islice(i1, 0, None, 2),
                              islice(i2, 1, None, 2)):

        
        np, jl, jh = [int(i) for i in nlh.rstrip('\n').split(' ')]
        #freqs = [int(i) for i in line.rstrip('\n').split(' ')]
        freqs = set([int(i) for i in line.rstrip('\n').split(' ')])

        found = "NO"
        for j in xrange(jl, jh+1):
            y = 0
            for f in freqs:
                if (f >= j and  f % j == 0 )or (f < j and  j % f == 0 ):
                    y += 1
                
            if y == len(freqs):
                found = j
                break


        logit(case, found)


if __name__ == '__main__':
    test()
