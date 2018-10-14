#!/usr/bin/python2
from sortedcontainers import SortedDict

def solve():
    n, k = map(int, raw_input().split())
    free_sizes = SortedDict()
    free_sizes[n] = 1
    def lr(x):
        return x-1-(x-1)/2, (x-1)/2
    while k > 0:
        n = free_sizes.iloc[-1]
        k -= free_sizes[n]
        l, r = lr(n)
        if l not in free_sizes:
            free_sizes[l] = free_sizes[n]
        else:
            free_sizes[l] += free_sizes[n]
        if r not in free_sizes:
            free_sizes[r] = free_sizes[n]
        else:
            free_sizes[r] += free_sizes[n]
        del free_sizes[n]
    return l, r
    

T = int(raw_input())
for i in range(T):
    print "Case #%d:" % (i+1), " ".join(map(str, solve()))
