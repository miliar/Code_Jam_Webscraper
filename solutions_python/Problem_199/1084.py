# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:47:48 2017

@author: Doris
"""

def flip(i):
    if(i == '+'):
        return '-'
    return '+'


T = int(input())
for t in range(T):
    temp = input().split(" ")
    S = list(temp[0])
    K = int(temp[1])
    length = len(S)
    
    count = 0
    for i in range(length):
        if(i+K > length and S[i] == '-'):
            count = -1
            break
        if(S[i] == '-'):
            count += 1
            for j in range(K):
                S[i+j] = flip(S[i+j])
        #print(S)
    if(count == -1):
        out = "Case #%d: IMPOSSIBLE"%(t+1)
    else:
        out = "Case #%d: %d"%(t+1, count)
    print(out)