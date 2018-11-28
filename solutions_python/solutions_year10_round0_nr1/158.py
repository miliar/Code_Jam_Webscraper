#!/usr/bin/env python

import sys
line = sys.stdin.readline()
data = [map(int, line.split()) for line in sys.stdin.readlines()]

i=0
for p, q in data:
    i += 1
    if not ((q + 1) % 2**p):
        print 'Case #%i: ON' % i
    else:
        print 'Case #%i: OFF' % i
