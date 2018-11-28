#!/usr/bin/env python

import os
import sys
import bisect

def time_to_int(time):
    h = int(time[0:2])
    m = int(time[3:5])
    return 60*h + m

def main():
    for ii in xrange(int(raw_input())):
        T = int(raw_input())
        
        (NA, NB) = tuple(map(int, raw_input().split(" ")))
        A = []
        B = []
        
        for i in xrange(NA):
            (a, b) = tuple(map(time_to_int, raw_input().split(" ")))
            A.append((a, 1))
            B.append((b+T, -1))
        
        for i in xrange(NB):
            (b, a) = tuple(map(time_to_int, raw_input().split(" ")))
            A.append((a+T, -1))
            B.append((b, 1))

        A.sort()
        B.sort()

        m = t = 0
        for (j, i) in A:
            t += i
            m = max(t, m)
        mA = m

        m = t = 0
        for (j, i) in B:
            t += i
            m = max(t, m)
        mB = m
        
        print "Case #%d: %d %d" % (ii+1, mA, mB)

if __name__ == '__main__':
    main()