#!/usr/bin/env python

from math import sqrt, floor

def f(r, t):
    k = floor((sqrt((2*r-1)**2+8*t)-(2*r-1))/4.0)
    if (2*r-3)*k+2*(k*k+k) <= t:
        return k
    else:
        return (k-1) 

if __name__ == '__main__':
    T = int(raw_input())
    for test in range(1,T+1):
        r, t = map(int, raw_input().split())
        print 'Case #%d: %d'%(test, f(r,t))
