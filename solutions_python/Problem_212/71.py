#!/usr/bin/env python

import sys
ls = sys.stdin.readlines()
nc = int(ls[0])
ls = ls[1:]
for C in range(nc):
    n, p = [int(x) for x in ls[0].split()]
    gs = [int(x) for x in ls[1].split()]
    ls = ls[2:]

    fs = {0: [], 1: [], 2: [], 3: []}
    for g in gs:
        f = g % p
        if f not in fs:
            fs[f] = []
        fs[f].append(g)
        
    ans = len(fs[0])
    r = 0
    def pick(f):
        global r
        global ans
        if r == 0:
            ans += 1
        r = (r + f[0]) % p
        f.pop(0)
    if p == 4:
        while len(fs[3]) and len(fs[1]):
            pick(fs[1])
            pick(fs[3])
        while len(fs[2]) > 1:
            pick(fs[2])
            pick(fs[2])
        while len(fs[1]) > 1 and len(fs[2]):
            pick(fs[1])
            pick(fs[1])
            pick(fs[2])
        while len(fs[1]):
            pick(fs[1])
        while len(fs[2]):
            pick(fs[2])
        while len(fs[3]):
            pick(fs[3])
    else:
        while len(fs[1]) and len(fs[2]):
            pick(fs[1])
            pick(fs[2])
        while len(fs[1]):
            pick(fs[1])
        while len(fs[2]):
            pick(fs[2])
    print "Case #%d: %d" % (C+1, ans)

