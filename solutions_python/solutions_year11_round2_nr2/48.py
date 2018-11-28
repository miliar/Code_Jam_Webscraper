#!/usr/bin/env python
# coding=utf-8
from __future__ import division
from sys import stdin

OO = 10**9

def check(pts, d, t):
    left = -OO
    for p, v in pts:
        #print("\t({0}, {1}), left:{2}".format(p,v,left))
        l = max(left, p-t)
        r = d*(v-1)+l
        if r > p+t:
            return False
        left = r+d
    return True

def solve(caseNo):
    res = 0
    c,d = map(int, stdin.readline().split())
    pts = sorted([ tuple(map(int, stdin.readline().split())) for i in range(c) ])
    low, high = 0, OO
    while high-low > 0.000000001:
        mid = (low+high)/2
        ok = check(pts,d,mid)
        #print("check({0}, {1}, {2}):{3}".format(pts, d, mid, ok))
        if ok:
            high = mid
        else:
            low = mid
    res = (high+low)/2
    print("Case #{0}: {1:.9f}".format(caseNo,res))

if __name__ == "__main__":
    cases = int(stdin.readline().strip())
    for i in range(cases):
        solve(i+1)
