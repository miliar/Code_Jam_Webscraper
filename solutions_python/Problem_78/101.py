#!/usr/bin/env python3

from fractions import gcd

def calc(n, pd, pg):
        if 100 // gcd(pd, 100) > n:
                return False
        if pg == 100 and pd < 100:
                return False
        if pg == 0 and pd > 0:
                return False
        return True

t = int(input())
for i in range(t):
        (n, pd, pg) = [int(a) for a in input().split()]
        print("Case #{0}: {1}".format(i+1, 'Possible' if calc(n, pd, pg) else 'Broken'))
