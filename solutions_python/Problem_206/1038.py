# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:33:57 2017

@author: arena
"""

T = int(input())

for t in range(T):
    D, N = [int(_) for _ in input().split(' ')]
    ks = []
    for n in range(N):
        ki, si = [int(_) for _ in input().split(' ')]
        ks.append((D-ki)/si)
    print("Case #" + str(t+1) + ": ", end = "")
    print(D / max(ks))