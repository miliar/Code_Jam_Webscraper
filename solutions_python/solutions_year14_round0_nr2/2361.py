#!/usr/bin/env python2

T = input()

for TT in range(1, T + 1):
    C, F, X = map(float, raw_input().split())
    R = 2.0
    NowT = 0.0
    while NowT + X / R > NowT + (C / R) + (X / (R + F)):
        NowT += (C / R)
        R += F
    NowT += X / R;
    print "Case #%d: %0.7lf" % (TT, NowT)
