#!/usr/bin/env python
#coding=utf-8

# Last Change: 2010-05-08 17:23:44

import sys

f = file(sys.argv[1])
ncase = int(f.readline())

for nncase in range(ncase):
    (r,k,n) = [int(x) for x in f.readline().split()]
    #print r,k,n

    g = [int(x) for x in f.readline().split()]
    #print g

    all = sum(g)
    if all <= k:
        print "Case #%d: %d"%(nncase+1,all*r)
        continue

    # analyze data
    i = 0
    m = []

    while i < n:
        j = v = 0
        while j < n:
            c = (i+j) % n
            x = g[c]
            if v+x > k:
                break
            else:
                v += x
            j += 1
        m.append((v, (i+j)%n))
        i += 1
    
    # r < n
    if r < n:
        i = 0
        su = 0
        cur = 0
        while i < r:
            su += m[cur][0]
            cur = m[cur][1]
            i += 1
        print "Case #%d: %d"%(nncase+1,su)
        continue

    # analyze loop
    cur = 0
    su1 = 0
    se = set()

    # first loop
    i = 0
    while i < r:
        su1 += m[cur][0]
        se.add(cur)
        cur = m[cur][1]
        if cur in se:
            break
        i += 1

    firstloop = i + 1
    loopnum = cur

    # loop 
    i = 0
    suloop = 0
    cur = loopnum
    while True:
        i += 1
        suloop += m[cur][0]
        cur = m[cur][1]
        if cur == loopnum:
            break
    looplen = i
    loopsum = suloop
    
    #print firstloop, su1
    #print loopnum, looplen, loopsum

    if firstloop == r:
        print "Case #%d: %d"%(nncase+1,su1)
    elif firstloop > r:
        i = 0
        su = 0
        while i < r:
            su += m[cur][0]
            cur = m[cur][1]
            i += 1
        print "Case #%d: %d"%(nncase+1,su)
    else:
        remain = r - firstloop
        loopsu = remain / looplen * loopsum

        lastloop = remain % looplen

        i = 0
        lastloopsum = 0
        cur = loopnum
        while i < lastloop:
            lastloopsum += m[cur][0]
            cur = m[cur][1]
            i += 1

        largesum = su1 + loopsu + lastloopsum
        print "Case #%d: %d"%(nncase+1,largesum)
    
f.close()
