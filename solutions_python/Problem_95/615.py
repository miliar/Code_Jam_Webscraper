#!/usr/bin/env python

import sys

rosetta1 = ("a zoo" , "y qee")
rosetta2 = ("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi")
rosetta3 = ("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
rosetta4 = ("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
rosetta5 = ("q", "z")

rosettastone = [rosetta1, rosetta2, rosetta3, rosetta4, rosetta5]

r = {}
rr = {}

for (e,g) in rosettastone:
    for i in range(len(e)):
        r[g[i]] = e[i]
        rr[e[i]] = g[i]

"""
for i in sorted(r.keys()):
    print i, " -> ", r[i]

for i in sorted(rr.keys()):
    print i, " -> ", rr[i]
"""

def translate(s, r):
    o = []
    for i in s:
        o.append(r[i])
    return "".join(o)
    
lines = sys.stdin.readline()
c = 1
for i in sys.stdin:
    print "Case #%d:" % (c), translate(i.strip(), r)
    c = c+1
