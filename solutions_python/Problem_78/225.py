# -*- coding: utf-8 -*-

from fractions import gcd

T = int(raw_input())
for case in xrange(1, T + 1):
    N, PD, PG = map(int, raw_input().split(' '))

    if PG == 100:
        if PD < 100:
            print 'Case #%d: Broken' % case
        else:
            print 'Case #%d: Possible' % case
        continue
    if PG == 0:
        if PD > 0:
            print 'Case #%d: Broken' % case
        else:
            print 'Case #%d: Possible' % case
        continue

    gD = gcd(PD, 100)
    gG = gcd(PG, 100)
    w, D = PD / gD, 100 / gD
    W, G = PG / gG, 100 / gG

    if D <= N:
        print 'Case #%d: Possible' % case
    else:
        print 'Case #%d: Broken' % case

