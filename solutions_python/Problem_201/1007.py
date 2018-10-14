#!/usr/bin/python

# Heapq is min heap, so we use -x to represent x
from heapq import *

def go(N, K):
    import pdb
    #pdb.set_trace()
    pq = []
    heappush(pq, 0) # dummy item
    heappush(pq, -N)
    Max = Min = None
    for i in xrange(K):
        val = -heappop(pq) - 1
        Max = val / 2 + val % 2
        Min = val / 2
        heappush(pq, -Max)
        heappush(pq, -Min)
    return Max, Min

def main():
    T = int(raw_input())
    for i in xrange(T):
        N, K = map(int, raw_input().split(' '))
        Max, Min = go(N, K)
        print "Case #%d: %d %d" % (
            i + 1,
            Max,
            Min,
        )
        
if __name__ == "__main__":
    main()
