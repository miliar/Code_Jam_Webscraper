#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from bisect import bisect_left

def solve():
    N = int(raw_input())
    A = sorted(float(x) for x in raw_input().split()) 
    B = sorted(float(x) for x in raw_input().split())

    #ans = 0
    #for _ in range(N):

    war(B[:], A[:], N)
    deceitful_war(A[:], B[:], N)

def war(A, B, N):
    ans = 0
    for _ in range(N):
        p = A.pop(0)
        r = bisect_left(B, p)
        if r == len(B):
            q = B.pop(0)
        else:
            q = B.pop(r)
        if p > q:
            ans += 1
    print N - ans,

def deceitful_war(A, B, N):
    ans = 0
    for _ in range(N):
        p = A.pop(0)
        r = bisect_left(B, p)
        if r == len(B):
            q = B.pop(0)
        else:
            q = B.pop(r)
        if p > q:
            ans += 1
    print ans

def main():
    N = int(raw_input())

    for i in range(N):
        print "Case #%d:" % (i + 1),
        solve() 

if __name__ == '__main__':
    main()
