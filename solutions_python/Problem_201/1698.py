import sys
import numpy as np
import math


def last_interval(n, k):
    
    gaps = { n : 1 }

    p = 1
    while p*2-1<k:
        _gaps = gaps.copy()
        # print(p,k)
        # print(gaps)
        for g in _gaps:
            lg = math.floor((g-1)/2)
            rg = g - lg - 1
            
            if lg not in gaps:
                gaps.update({lg:0})

            if rg not in gaps:
                gaps.update({rg:0})


            gaps[lg] += gaps[g]
            gaps[rg] += gaps[g]

            del gaps[g]
        p*=2
    k -= (p - 1)

    # print(gaps)

    keys = reversed(sorted(gaps.keys()))

    for g in keys:
        k -= gaps[g]
        if k<1:
            lg = math.floor((g-1)/2)
            rg = g - lg - 1
            return max(lg, rg), min(lg, rg)


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for i in xrange(t):
    	n, k = f.readline().split()
        n = long(n)
        k = long(k)
        
    	mx, mn = last_interval(n, k)

    	print("Case #{0}: {1} {2}".format(i+1, int(mx), int(mn)))
