#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
rl = lambda: sys.stdin.readline().strip()
cases = int(rl())
for cc in xrange(cases):
    it = iter(rl().split())
    c = int(it.next())
    combines = {}
    opposes = set()
    for i in xrange(c):
        a,b,c = it.next()
        combines[a+b] = combines[b+a] = c
    d = int(it.next())
    for i in xrange(d):
        a,b = it.next()
        opposes.add(a+b)
        opposes.add(b+a)
    it.next()
    q = []
    for chr in it.next():
        if q:
            lq = q[-1] + chr
            if lq in combines:
                q.pop()
                q.append(combines[lq])
            else:
                clear = False
                for c in q:
                    if (c+chr) in opposes:
                        clear = True
                if clear:
                    q = []
                else:
                    q.append(chr)
        else:
            q.append(chr)

    print "Case #%d: [%s]" % (cc+1, ", ".join(q))
