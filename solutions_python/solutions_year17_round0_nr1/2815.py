#!/bin/python3

import sys

def flip(pans):
    new_pans = ""
    for pan in pans:
        if pan == '+':
            new_pans = new_pans + '-'
        else:
            new_pans = new_pans + '+'
    return new_pans[:]
    

def analyze(pans):
    l = len(pans)
    flips = 0
    for i in range(l-k+1):
        if pans[i] == '-':
            flips += 1
            pans = pans[:i] + flip(pans[i:i+k]) + pans[i+k:]
    for pan in pans[-k+1:]:
        if pan == '-':
            return 'IMPOSSIBLE'
    return str(flips)
            
t = int(input().strip())
for a0 in range(t):
    pancakes, k = input().strip().split()
    k = int(k)
    print("Case #" + str(a0+1) + ": " + analyze(pancakes))