#!/usr/bin/env python

import sys

def solve(N, K):
    if K == 1:
        assert N >= 1
        return ((N - 1) / 2, (N - 1) / 2) if N % 2 != 0 else ((N/2), (N/2)-1)
    K -= 1
    half_K = (K / 2) if K % 2 == 0 else (1 + (K-1)/2)
    if N % 2 == 0:
        if K % 2 == 0:
            return solve(N / 2 - 1, half_K)
        else:
            return solve(N / 2, half_K) # NOTE: is it really always worse than solve(N/2-1, K - half_K)?
    else:
        return solve((N - 1)/2, half_K)

import heapq
    
def solve_naive(N, K):
    intervals = [-N]
    while K > 1:
        K -= 1
        cur = -heapq.heappop(intervals)
        if cur % 2 == 0:
            heapq.heappush(intervals, -cur / 2)
            heapq.heappush(intervals, -(cur / 2 - 1))
        else:
            heapq.heappush(intervals, -(cur-1) / 2)
            heapq.heappush(intervals, -(cur-1) / 2)
    last = -heapq.heappop(intervals)
    if last % 2 == 0:
        return last / 2, (last-1)/2
    else:
        return (last-1)/2, (last-1)/2

if __name__ == "__main__":
    inp = open(sys.argv[1], 'r').readlines()
    T = int(inp[0])
    for t in xrange(T):
        N, K = map(int, inp[t+1].strip().split())
        S_max, S_min = solve(N, K)
        #S_max_naive, S_min_naive = solve_naive(N, K)
        #assert (S_max, S_min) == (S_max_naive, S_min_naive), (N, K, S_max_naive, S_min_naive, S_max, S_min)
        print "Case #%d: %d %d" % (t+1, S_max, S_min)
