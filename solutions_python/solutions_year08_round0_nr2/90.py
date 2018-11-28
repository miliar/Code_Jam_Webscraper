#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline())
for case in xrange(cases):
    t = int(sys.stdin.readline())
    n = [int(x) for x in sys.stdin.readline().split()]
    need = [[0] * (24*60) for i in [0, 1]]
    ready = [[0] * (24*60) for i in [0, 1]]
    for i in [0, 1]:
        for j in xrange(n[i]):
            line = sys.stdin.readline().split()
            t1 = sum(a*b for (a, b) in zip([60, 1], [int(x, 10) for x in line[0].split(':')]))
            t2 = sum(a*b for (a, b) in zip([60, 1], [int(x, 10) for x in line[1].split(':')]))
            need[i][t1] += 1
            if t2+t < 24*60:
                ready[1-i][t2+t] += 1
    waiting = [0, 0]
    cnt = [0, 0]
    for x in xrange(24*60):
        for i in [0, 1]:
            waiting[i] += ready[i][x]
            diff = waiting[i] - need[i][x]
            if diff >= 0:
                waiting[i] = diff
            else:
                cnt[i] += abs(diff)
                waiting[i] = 0
    print 'Case #%d: %d %d' % (case+1, cnt[0], cnt[1])
