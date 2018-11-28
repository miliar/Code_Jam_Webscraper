#!/usr/bin/env pypy

import math
import sys


def rec(s, k):
    for z in range(k):
        lss = list(s)
        rss = list(s)
        lss[0] = -1
        rss[-1] = -1
        for i in range(1, len(s) - 1):
            lss[i] = -1 if s[i] else lss[i - 1] + 1
        for i in range(len(s) - 2, 0, -1):
            rss[i] = -1 if s[i] else rss[i + 1] + 1
        #print s
        #print lss, rss
        bm = None
        bs = []
        for i in range(1, len(s) - 1):
            m = min(lss[i], rss[i])
            if bm is None or m > bm:
                bs = [i]
                bm = m
            elif m == bm:
                bs.append(i)
        if len(bs) == 1:
            p = bs[0]
        else:
            bn = max(max(lss[i], rss[i]) for i in bs)
            bt = [i for i in bs if max(lss[i], rss[i]) == bn]
            p = bt[0]
        s[p] = True
        #x = int(2 ** ((math.log(len(s) - 1) / math.log(2)) - math.floor(math.log(z + 1) / math.log(2)) - 1))
        #print ''.join('O' if t else '.' for t in s), ' '.join('%4d' % n for n in [lss[p], rss[p], lss[p] + 1, rss[p] + 1, x, lss[p] + 1 - x, rss[p] + 1 - x])
    return max(lss[p], rss[p]), min(lss[p], rss[p])


def go(n, k):
    return rec([True] + [False] * n + [True], k)


for i, l in enumerate(sys.stdin.read().splitlines()[1:]):
    n, k = l.split(' ', 1)
    n = int(n)
    k = int(k)
    r = go(n, k)
    print 'Case #%d: %d %d' % ((i + 1,) + r)

#for k in range(1, 100):
#    print k
#    print go(k, k)
