#!/usr/bin/python3

import sys
import math

epsilon = 0.0000000001

def case():
    C, F ,X = [float(x) for x in sys.stdin.readline().split()]
    def sec(k):
        r = 0
        for i in range(k): r += C/(2+i*F)
        return r
    c = max(0,X/C - 1 - 2/F)
    k = math.ceil(c)
    if float(k) - c > 1- epsilon: k -= 1
    return sec(k) + X/(2+k*F)


T = int(sys.stdin.readline())
for i in range(1,T+1):
    print("Case #%s: %s" % (i, case()))
    

