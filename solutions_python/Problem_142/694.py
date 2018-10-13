# -*- coding: utf-8 -*-

import math

def en(a):
    res = []
    h = ''
    hh = 0
    for e in a:
        if e == h:
            hh += 1
        else:
            res.append((h, hh))
            h = e
            hh = 1
    res.append((h, hh))
    return res

def solve(n, a):
    res = 0
    ena = []
    for e in a:
        ena.append(en(e))
    cnt = 0
    maxcnt = max([len(e) for e in ena])
    while cnt < maxcnt:
        try:
            r = [e[cnt] for e in ena]
        except:
            return 'Fegla Won'
        if len(set([e[0] for e in r])) == 1 and len(r) == n:
            m = sum([e[1] for e in r]) / n
            res += sum([abs(e[1] - m) for e in r])
        else:
            return 'Fegla Won'
        cnt += 1
    return str(res)

t = int(raw_input())

for i in xrange(1, t+1):
    n = int(raw_input())
    a = []
    for j in xrange(n):
        a.append(raw_input())
    print 'Case #%d: %s' % (i, solve(n, a))
