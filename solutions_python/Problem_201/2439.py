#import string,itertools,fractions,heapq,re,array,bisect
#from math import *
from collections import defaultdict
def rl(s): return xrange(len(s))


INF = 2147483647


import sys
stdin = sys.stdin

T =        int( stdin.readline().strip() )

for icase in range(1, T+1):
    N, K = map(int, stdin.readline().strip().split())

    span_sizes2counts = defaultdict(int)
    span_sizes2counts[N] = 1
    occupied = 0
    while True:
        large_span = max(span_sizes2counts.keys())
        if 0 == large_span:
            break
        large_span_count = span_sizes2counts[large_span]
        del span_sizes2counts[large_span]

        if occupied < K <= occupied + large_span_count:
            print "Case #%d:" % icase, large_span//2, (large_span-1)//2
            break
        span_sizes2counts[(large_span-1)//2] += large_span_count
        span_sizes2counts[large_span//2] += large_span_count

        occupied += large_span_count


