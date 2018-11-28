#!/usr/bin/env python
#-*- encoding: utf-8 -*-

def intersects(a1, b1, a2, b2):
    return ((a1 > a2) and (b1 < b2)) or ((a1 < a2) and (b1 > b2))

T = input()
for t in xrange(1, T+1):
    N = input()
    lines = [tuple(int(x) for x in raw_input().split()) for i in xrange(N)]

    cnt = 0
    already_done = set()
    for l in lines:
        for l2 in lines:
            if l == l2: continue
            if (l2, l) in already_done: continue
            if intersects(l[0], l[1], l2[0], l2[1]):
                cnt += 1
                already_done.add((l, l2))
    print 'Case #%d: %d' % (t, cnt)
