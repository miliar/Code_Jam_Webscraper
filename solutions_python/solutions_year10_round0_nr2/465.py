#!/usr/bin/env python
#coding=utf-8

# Last Change: 2010-05-09 00:27:48

import sys

f = file(sys.argv[1])
ncase = int(f.readline())

for nncase in range(ncase):
    t = [ int(x) for x in f.readline().split()[1:] ]
    t.sort()
    #print t

    tdup = []
    i = 1
    while i < len(t):
        if t[i-1] == t[i]:
            tdup.append(t[i])
        i += 1

    for x in tdup:
        t.remove(x)

    # pace
    t2 = [ t[i+1]-t[i] for i in range(len(t)-1) ]
    t2.sort()
    #print t2

    if len(t) == 2:
        y = 0
        #d = t[1] - t[0]
        d = t2[0]
        x = t[-1] / d
        if t[-1] % d <> 0:
            x += 1
        while True:
            y = d * x - t[-1]
            ok = True
            for tt in t[:-1]:
                if ((y + tt) % d) <> 0:
                    ok = False
                    break
            if ok:
                break
            x += 1
        #print d
        print "Case #%d: %d"%(nncase+1,y)
        continue

    # n > 2
    # all are odd or even
    ###same = True
    ###for x in t2:
    ###    if x % 2 <> 0:
    ###        same = False
    ###        break
    ###if not same:
    ###    print "Case #%d: %d"%(nncase+1,0)
    ###    continue

    i = 1
    while i <= t2[0]:
        dv = t2[0]
        if t2[0] % i == 0:
            dv /= i
        ok = True
        for x in t2[1:]:
            if x % dv <> 0:
                ok = False
                break
        if ok:
            break
        i += 1

    y = 0
    d = t2[0] / i
    x = t[-1] / d
    if t[-1] % d <> 0:
        x += 1
    while True:
        y = d * x - t[-1]
        ok = True
        for tt in t[:-1]:
            if ((y + tt) % d) <> 0:
                ok = False
                break
        if ok:
            break
        x += 1
    #print d
    print "Case #%d: %d"%(nncase+1,y)

f.close()
