#!/usr/bin/python

import sys
from decimal import *

def solve(horses, D, N):
    maxTime = Decimal(0)
    for i in range(N):
        d = Decimal(D)-Decimal(horses[i][0])
        s = Decimal(horses[i][1])
        maxTime = max(maxTime, d/s)
        #print("D = {:} - dist {:} = {:} ".format(Decimal(D), Decimal(horses[i][0]), d))
        #print("dist {:} /speed {:}  = {:}".format(d, s, d/s))

        #print("maxtime = {:}".format(maxTime))

    return Decimal(D)/Decimal(maxTime)


getcontext().prec = 9

with open(sys.argv[1], 'r') as f:
    cases = int(f.readline())
    for case in range(cases):
        D, N = map(int, f.readline().split())
        horses = []
        for i in range(N):
           a =  list(map(int, f.readline().split()))
           horses.append(a)
        #print(horses)
        ans = solve(horses, D, N)
        print("Case #{:}: {:.6f}".format(case+1, Decimal(ans))) 
