#!/usr/bin/env python3

import sys, os, re
import numpy as np
import math
from collections import defaultdict

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    T = int(input().strip())
    for t in range(1, T+1):
        N, K = [int(x) for x in input().strip().split(" ")]
        R = np.zeros((N,))
        H = np.zeros((N,))
        for i in range(N):
            R[i], H[i] = [int(x) for x in input().strip().split(" ")]
            
        sidesurface = H * 2*np.pi*R
        ssord = np.argsort(sidesurface)[::-1][:K]
        rord = np.argsort(R)[::-1]

        rmax = np.max(R[ssord])
       
        for i in range(len(rord)):
            if R[rord[i]] <= rmax:
                break
            else:
                plusface = np.pi*R[rord[i]]**2 - np.pi*rmax**2 + sidesurface[rord[i]] - sidesurface[ssord[-1]]
                if (rord[i] not in ssord) and plusface > 0: #swap in rord
                    ssord[-1] = rord[i]
                    break
        
        rmax = np.max(R[ssord])
        
        ans = np.sum(sidesurface[ssord])
        ans += np.pi * rmax**2
        print("Case #{}: {}".format(t, ans))

if __name__ == '__main__':
    main()
