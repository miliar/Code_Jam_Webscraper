#!/usr/bin/env python3.1

import collections
import sys

def readline():
    return next(sys.stdin).strip()

def readvals(t):
    return map(t, readline().split())

def euros(nrides, capacity, groups):
    gid2rides = {}
    rides2euros = {}
    toteuros = 0

    for ride in range(1, nrides + 1):
        left = capacity
        groups_in = 0
        for gid, groupsize in groups:
            if left < groupsize:
                break
            left -= groupsize
            groups_in += 1
#        print("DEBUG: enter {}".format(list(groups)[:groups_in]))
        groups.rotate(-groups_in)
        toteuros += capacity - left
        
        if gid in gid2rides:
            oldride = gid2rides[gid]
            period_len = ride - oldride
            period_val = toteuros - rides2euros[oldride]
            # print("DEBUG: period found!"
            #       "(from {}, length {}, value {}".format((gid, oldride),
            #                                              period_len,
            #                                              period_val))
            periods, rest = divmod(nrides - ride, period_len)
            
            return (toteuros + periods * period_val +
                    rides2euros[oldride + rest] - rides2euros[oldride])
        
        gid2rides[gid] = ride
        rides2euros[ride] = toteuros
        
    return toteuros

for i in range(int(readline())):
    rides, capacity, N = readvals(int)
    groups = collections.deque(enumerate(readvals(int)))
    assert N == len(groups)
    
    print('Case #{}: {}'.format(i + 1, euros(rides, capacity, groups)))
