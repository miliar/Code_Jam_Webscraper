# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:54:02 2017

@author: Özcan
"""

def flip(S, K, pos):
    for i in range(K):
        if S[pos+i]== '+':
            S = S[:pos+i] + '-' + S[pos+i+1:]
        else:
            S = S[:pos+i] + '+' + S[pos+i+1:]
    return S

def solve(S,K):
    size= len(S)
    counter = 0
    pos=0
    while True:
        pos = S.find('-', pos)
        if pos == -1:
            return counter
        if pos > size-K:
            return 'IMPOSSIBLE'
        S = flip(S, K, pos)
        counter += 1
        pos += 1
        
        
numberCases = int(input())

for i in range(1,numberCases+1):
    S, K = [s for s in input().split(" ")]
    result = solve(S, int(K))
    print("Case #{}: {}".format(i, result))