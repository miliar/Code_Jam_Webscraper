#!/usr/bin/env python3
import sys
from decimal import Decimal


def rint():
    return map(int, input().split())

T = int(input())
for ii in range(T):
    r = [0,0,0,0]
    ans = 0
    N, P = rint()
    G = list(rint())
    for i in G:
        r[i%P] += 1
    if P == 2:
        ans = r[0] + r[1]//2
        if r[1]%2:
            ans+=1
    elif  P == 3:
        ans = r[0] + min(r[1], r[2]) + abs(r[2]-r[1])//3
        if abs(r[2]-r[1])%3:
            ans += 1
    else:
        ans = r[0] + min(r[1], r[3]) + r[2]//2
        r13 = abs(r[1]-r[3])
        r2 = r[2]%2
        if r2:
            ans +=1
            if r13 == 2:
                pass
            elif r13 > 2:
                r13 -=2
                ans += (r13)//4
                if (r13)%4:
                    ans+=1
        else:
            ans += r13//4
            if r13%4:
                ans+=1

    print("Case #%d:"%(ii+1), ans)
