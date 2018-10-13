#!/usr/bin/env python3

from heapq import *

def stalls(N,K):
    IntSize = [-N]
    IntCount = {}
    IntCount[N] = 1
    while K>0:
        s = -heappop(IntSize)
        assert(IntCount[s]>0)
        k = min(K,IntCount[s])
        K -= k
        IntCount[s] -= k
        if IntCount[s]==0:
            del IntCount[s]
        l = (s-1)//2
        if l>0:
            if l not in IntCount:
                heappush(IntSize,-l)
                IntCount[l] = 0
            IntCount[l] += k
        r = s-1-l
        if r>0:
            if r not in IntCount:
                heappush(IntSize,-r)
                IntCount[r] = 0
            IntCount[r] += k
        ll,lr = l,r
    return (ll,lr)

def main():
    T = int(input())
    for t in range(1,T+1):
        N,K = map(int,input().split())
        z,y = stalls(N,K)
        print('Case #%d: %d %d' % (t,y,z))

main()
