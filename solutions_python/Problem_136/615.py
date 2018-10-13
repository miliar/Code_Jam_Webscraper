#!/usr/bin/python

import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    C, F, X = tuple([float(x) for x in sys.stdin.readline().split()])
    fc = 2
    tf = C / fc
    tx = X / fc
    t = tf + X / (fc + F)
    while(t < tx):
        tx = t
        fc = fc + F
        tf = tf + C / fc
        t = tf + X / (fc + F)
    print('Case #%d: %.7f' % (i, tx))
