#!/usr/bin/env python3
from functools import reduce
def verify():
    pass

def solve(N,K):
    units = float(input())
    p=[float(x) for x in input().split()]
    p.sort()
    for i in range(K-1):
        diff=p[i+1]-p[i]
        cangive=min(diff*(i+1),units)
        for j in range(i+1):
            p[j]+=cangive/(i+1)
        units-=cangive
    if units>0:
        p=[p[i]+units/K for i in range(K)]
    return reduce(lambda x,y: x*y,p)

if __name__=='__main__':
    t = int(input())
    for cas in range(1,t+1):
        ans = solve(*map(int,input().split()))
        print("Case #{}: {}".format(cas,ans))
