#!/usr/bin/env python3

import sys, os, re
import numpy as np
import math

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_maxmin_init(N, K):
    alld = []
    cache = {}

    def get_maxmin(N, K, level=0):
        #print("%sN=%d, K=%d" % ("  " * level, N, K))
        if K == 1:
            dmin, dmax = (math.floor((N-1)/2), math.ceil((N-1)/2))
            alld.append((dmin, dmax))
            #print("%s->dmin=%d, dmax=%d" % ("  " * level, dmin, dmax))
            return dmin, dmax
        if K == 0:
            return 2e18, 2e18 
        if (N, K) in cache:
            dmin, dmax = cache[(N, K)]
            alld.append((dmin, dmax))
            #print("%s->dmin=%d, dmax=%d" % ("  " * level, dmin, dmax))
            return dmin, dmax
        a = get_maxmin(math.ceil((N-1)/2), math.ceil((K-1)/2), level=level+1)
        b = get_maxmin(math.floor((N-1)/2), math.floor((K-1)/2), level=level+1)
        dmin, dmax = sorted([a, b])[0]

        alld.append((dmin, dmax))
        cache[(N, K)] = (dmin, dmax)
        #print("%s->dmin=%d, dmax=%d" % ("  " * level, dmin, dmax))
        return dmin, dmax
    
    get_maxmin(N, K)
    dmin, dmax = sorted(alld)[0]
    #log(alld)
    return dmin, dmax

def main():
    T = int(input().strip())
    for t in range(1, T+1):
        N, K = [int(x) for x in input().strip().split(" ")]

        dmin, dmax = get_maxmin_init(N, K)

        print("Case #{}: {} {}".format(t, dmax, dmin))

if __name__ == '__main__':
    main()
