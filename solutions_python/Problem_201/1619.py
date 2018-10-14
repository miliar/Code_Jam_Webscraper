from __future__ import print_function
import sys
import math

def getstalls(n, k):
    serve = k-1
    large = math.ceil((n-1)/2)
    small = math.floor((n-1)/2)
    if (n-1) % 2 == 0:
        largecount = 2
        smallcount = 0
    else:
        largecount = 1
        smallcount = 1
    if serve <= 0:
        return large, small
    while serve > 0:
        serve -= largecount
        if serve <= 0:
            return getstalls(large, 1)
        serve -= smallcount
        if serve <=0:
            return getstalls(small, 1)
        if large % 2 == 1:
            largecount = 2 * largecount + smallcount
        else:
            smallcount = largecount + 2 * smallcount
        large = math.ceil((large-1)/2)
        small = large-1
    return -1, -1

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for x in range(T):
        N, K = [int(x) for x in f.readline().split()]
        large, small = getstalls(N, K)
        print('Case #%d: %d %d' % (x+1, large, small))
