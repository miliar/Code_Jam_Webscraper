#!/usr/bin/env python3

from math import log, floor
from collections import OrderedDict
from operator import itemgetter

def get_dists(n):
    if n == 1:
        dl, dr = 0, 0
    elif n == 2:
        dl, dr = 0, 1
    else:
        dl = n//2 - (1 - n % 2) # if even subtract 1, if odd subtract 0
        dr = n//2                       # always floor(n/2)
    return dl, dr


def get_intervals(N, depth):
    leaves = N//int(2**depth) - 1
    intervals = defaultdict(int)
    if N % 2 == 0:
        intervals[leaves] += 2**depth-1
        intervals[leaves+1] += 1
    else:
        intervals[leaves] += 2**depth-2
        intervals[leaves+1] += 2
    return intervals


def rec(n, deg=1, depth=1, K=1):
    bfsq = [(n, deg)]
    tdegs = 0
    while tdegs <= K: # tdegs < 2**depth and 
        current_n, current_deg = bfsq.pop(0)
        if current_n % 2 == 0:
            bfsq.append((current_n//2-1, current_deg))
            bfsq.append((current_n//2,   current_deg))
        else:
            bfsq.append((current_n//2, 2*current_deg))

        d = OrderedDict()
        tdegs = 0
        for (ns, degs) in bfsq:
            if ns in d: d[ns] += degs
            else:       d[ns]  = degs
            tdegs += degs
        bfsq = sorted([(ns, degs) for (ns, degs) in d.items()], key=itemgetter(0), reverse=True)
        #print(tdegs, bfsq)
    return bfsq, current_n

T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    depth = floor(log(K+1, 2)) - 1
    Kdone = int(2**(depth+1)) - 1
    Ktodo = K - Kdone
    #print(N, K, depth, Kdone, Ktodo)
    tmp, last = rec(N, deg=1, depth=depth, K=K)
    dl, dr = get_dists(last)
    #print(tmp, last, dl, dr)
    print('Case #%d: %d %d'%(t, max(dl,dr), min(dl,dr)))
    



    #if (N == K):
    #    print('Case #%d: %d %d'%(t, 0, 0))
    #    continue
    
    #Kdone = int(2**(depth)) - 1
    #Ktodo = K - Kdone
    #if Kdone == 0:
    #    depth -= 1
    #    Kdone = int(2**(depth)) - 1
    #    Ktodo = K - Kdone
    #intervals = get_intervals(N, depth)
    #max_key = max(list(intervals.keys()))####

    #if t == 6: print(N, K, Kdone, intervals)
    #if Ktodo == 0:
    #    dl, dr = max(list(intervals.keys())), min(list(intervals.keys()))
    #else:
    #    while Ktodo > 0:
    #        max_key = max(list(intervals.keys()))
    #        intervals[max_key] -= 1
    #        if intervals[max_key] == 0:
    #            del intervals[max_key]
    #        Ktodo -= 1
    #    dl, dr = get_dists(max_key)
    #print('Case #%d: %d %d'%(t, max(dl,dr), min(dl,dr)))
       
