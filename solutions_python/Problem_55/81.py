#!/usr/bin/python
# -*- coding: utf-8 -*-

t = int(raw_input())
for c in range(1, t+1):
    [ridecount, capacity, n] = [int(x) for x in raw_input().split()]
    g = [int(x) for x in raw_input().split()]
    
    firsttime = [-1 for x in g]
    firstcash = [-1 for x in g]
    accumulator = 0
    pos = 0
    i = 0
    while i < ridecount:
        firsttime[pos] = i
        firstcash[pos] = accumulator
        
        ridesize = 0
        while ridesize + g[pos] <= capacity:
            ridesize += g[pos]
            pos += 1
            if pos == n:
                pos = 0
                if i == 0: break
        
        accumulator += ridesize
        i += 1
        
        if firsttime[pos] != -1:
            looplen = i - firsttime[pos]
            dotheloop = (ridecount - firsttime[pos]) / looplen
            i = firsttime[pos] + dotheloop * looplen
            accumulator = firstcash[pos] + dotheloop * (accumulator - firstcash[pos])
            firsttime = [-1 for x in g]
        
    
    print "Case #{0}: {1}".format(c, accumulator)
