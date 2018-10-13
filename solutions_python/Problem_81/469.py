# -*- coding: utf-8 -*-

from fractions import Fraction as F
import copy

T = int(raw_input())
for case in xrange(1, T + 1):
    N = int(raw_input())
    R = dict([(i, {}) for i in xrange(N)])
    for i in xrange(N):
        for j, c in enumerate(raw_input()):
            if c != '.':
                R[i][j] = c
    WP = [F(R[i].values().count('1'), len(R[i])) for i in xrange(N)]

    OWP = []
    for i in xrange(N):
        r = copy.deepcopy(R)
        for j in r[i]:
            if i in r[j]:
                del r[j][i]
        w = {}
        for j in r[i]:
            w[j] = F(r[j].values().count('1'), len(r[j]))
        OWP.append(sum(w.values()) / len(w))

    OOWP = []
    for i in xrange(N):
        r = copy.deepcopy(R)
        for j in r[i]:
            if i in r[j]:
                del r[j][i]
        s = [OWP[j] for j in r[i]]
        OOWP.append(sum(s) / len(s))

    print 'Case #%d:' % case
    for i in xrange(N):
        rpi = F(1, 4) * WP[i] + F(1, 2) * OWP[i] + F(1, 4) * OOWP[i]
        print '%.7f' % rpi

