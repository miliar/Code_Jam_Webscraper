# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 01:28:19 2017

@author: Özcan
"""


def solve(D, SK):
    max_t = 0
    result= 0
    for horse in KS:
        space = D - horse[0]
        t = space/horse[1]
        if t>max_t:
            max_t = t
            result = D/t
            
    return result


numberCases = int(input())

for i in range(1,numberCases+1):
    KS = []
    D, N = [int(s) for s in input().split(" ")]
    for n in range(N):
        KS = KS + [tuple(int(p) for p in input().split(" "))]
    result = solve(D, KS)
    print("Case #{}: {}".format(i, result))