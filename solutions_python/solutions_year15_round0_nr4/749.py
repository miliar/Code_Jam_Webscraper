#! /usr/bin/python

import os, sys, copy

def debug(msg):
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        sys.stderr.write('%s' % msg)
        sys.stderr.write('\n')


gab = 'GABRIEL'
rich = 'RICHARD'

T = int(sys.stdin.readline())
# For each test case
for t in range(1, T+1):
    res = None
    debug(' ************* case %s' % t)
    [X, R, C] = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    [R, C] = sorted([R, C]) # C > R
    if X >= 5: # this is C, which is 4 for the small
        res = rich
    elif (R * C) % X != 0:
        res = rich
    elif X > R and X > C:
        res = rich
    elif X > R * C:
        res = rich
    elif X == 1:
        res = gab
    elif X == 2:
        res = gab
    elif X == 3:
        if R == 1:
            res = rich
        else:
            res = gab
    else: # X == 4
        if R == 1:
            res = rich
        elif R == 2 and C == 4:
            res = rich
        else:
            res = gab
    debug('f %s' % ((R * C) % X != 0))
    sys.stdout.write('Case #%s: %s\n' % (t, res))
