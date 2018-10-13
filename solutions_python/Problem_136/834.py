#!/usr/bin/env python

import sys

def read_int():
    return int(sys.stdin.readline())

def read_float():
    return 

problems = read_int()

for p in range(1,problems+1):
    gain = float(2)
    (C,F,X) = [float(x) for x in sys.stdin.readline().split(' ')]
    so_far = 0.0
    next_gain = gain + F
    while (X/gain) > (C / gain + X / next_gain):
        so_far += C / gain
        gain += F
        next_gain = gain + F
    so_far += X/gain
    print 'Case #%i: %.7f' % (p,so_far) 
