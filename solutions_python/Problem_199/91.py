#!/usr/bin/env python3

import sys, os, re
import numpy as np

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

T = int(input().strip())
for t in range(1, T+1):
    S, K = input().strip().split(" ")
    K = int(K)
    S = np.array([False if x == '-' else True for x in S], dtype='bool')
    i = 0
    num_flips = 0
    while i <= len(S) - K:
        if ~S[i]:
            S[i:i+K] = ~S[i:i+K]
            num_flips += 1
        i += 1
    if np.all(S):
        ans = num_flips
    else:
        ans = "IMPOSSIBLE"
    #log("K: %d" % K)

    print("Case #{}: {}".format(t, ans))
    
