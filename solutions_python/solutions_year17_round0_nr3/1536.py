# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:36:16 2017

@author: Giovanni
"""

inp = open('C-small-2-attempt1.in','r')
t = int(inp.readline())
cases = [inp.readline()[:-1] for s in range(t)]


for c in range(t):
    n, k = [int(s) for s in cases[c].split(" ")]
    stalls = {n:1}
    x = 0
    while x < k:
        
        m = max(stalls)
        left = int((m/2.0) - 0.5) 
        right = m - left - 1 
        
        if stalls[m] > k - x:
            diff = k - x
        else:
            diff = stalls[m]
        
        if left in stalls:
            stalls[left] += diff
        else:
            stalls[left] = diff
            
        if right in stalls:
            stalls[right] += diff
        else:
            stalls[right] = diff
        
        stalls[m] -= diff
        if stalls[m] == 0:
            stalls.pop(m, None)
            
        x += diff
    
    print("Case #{}: {} {}".format(c+1, right, left))
