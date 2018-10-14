# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:27:21 2017

@author: Robbe Sneyders
"""

def flip(s, k, i):
    for j in range(i, i+k):
        if s[j] == '+':
            s[j] = '-'
        else:
            s[j] = '+'
        
    return s

def answer(s, k):
    
    flips = 0
    
    for i, c in enumerate(s):
        if c == '-':
            if len(s) - i < k:
                return 'IMPOSSIBLE'
                
            s = flip(s, k, i)
            flips += 1
            
    return flips
        

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    case = input().split(' ')
    s = list(case[0])
    k = int(case[1])
    print("Case #{}: {}".format(i, answer(s, k)))