#!/usr/bin/env python3

import sys, os, re
import numpy as np

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

T = int(input().strip())
for t in range(1, T+1):
    N = int(input().strip())
    Nstr = "0" + str(N)
    rerun = True
    while rerun:
        rerun = False
        for i in range(1, len(Nstr)):
            if Nstr[i-1] > Nstr[i]:
                N = int(Nstr) - (int(Nstr[i:]) + 1)
                Nstr = "0" + str(N)
                rerun = True
                break
    ans = N
    print("Case #{}: {}".format(t, ans))
    
