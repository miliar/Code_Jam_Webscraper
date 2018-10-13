#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys

def WP(s):
    games = 0
    won = 0
    for ch in s:
        if ch == '1':
            games += 1
            won += 1
        elif ch == '0':
            games += 1
    return float(won) / float(games)
def OWP(s, i):
    games = 0
    won = 0
    for _i in xrange(len(s)):
        if _i == i:
            continue
        if s[_i] == '1':
            games += 1
            won += 1
        elif s[_i] == '0':
            games += 1
    return float(won) / float(games)

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        if sys.argv[1] != '-':
            fn = sys.argv[1]
            f = open(fn)
    t = int(f.readline())
    for _t in xrange(t):
        sched = []
        wps = []
        owps = []
        oowps = []
        n = int(f.readline())
        for _n in xrange(n):
            sched.append(f.readline().strip())
        for i in xrange(n):
            wps.append(WP(sched[i]))
            owp = 0.0
            denom = 0.0
            for j in xrange(n):
                if i == j:
                    continue
                if sched[i][j] != '.':
                    owp += OWP(sched[j], i)
                    denom += 1
            owp /= denom
            owps.append(owp)
        for i in xrange(n):
            oowp = 0.0
            denom = 0.0
            for j in xrange(n):
                if i == j:
                    continue
                if sched[i][j] != '.':
                    oowp += owps[j]
                    denom += 1
            oowp /= denom
            oowps.append(oowp)
        print 'Case #{}: '.format(_t + 1)
        for i in xrange(n):
            print '{}'.format(wps[i] / 4.0 + owps[i] / 2.0 + \
            oowps[i] / 4.0)

