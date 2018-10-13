#!/usr/bin/python3

from sys import stdin
from fractions import gcd

def read():
    return tuple(map(int, stdin.readline().split()))

def verify(n, pd, pg):
    if pd < 100 and pg == 100: return False
    if pd > 0 and pg == 0: return False
    g = gcd(100, pd)
    return 100//g <= n

T, = read()
for nc in range(1, T+1):
    n, pd, pg = read()
    b = verify(n, pd, pg)
    print('Case #{}: {}'.format(nc, 'Possible' if b else 'Broken'))
