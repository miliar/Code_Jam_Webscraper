#!/usr/bin/env python

import sys
T = int(sys.stdin.readline())

for i in xrange(1, T + 1):
    N, M = [int(x) for x in sys.stdin.readline().split()]
    t = {}
    for j in xrange(N):
        d = sys.stdin.readline().strip()[1:]
        cd = t
        for n in d.split('/'):
            if n not in cd:
                cd[n] = {}
            cd = cd[n]

    create = 0
    for j in xrange(M):
        d = sys.stdin.readline().strip()[1:]
        cd = t
        for n in d.split('/'):
            if n not in cd:
                cd[n] = {}
                create += 1
            cd = cd[n]

    print 'Case #%i: %s' % (i, create)
