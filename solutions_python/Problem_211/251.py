# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:19:19 2017

@author: Robbe Sneyders
"""

import numpy as np

def answer(n, k, u, p):
    
    while u > 0.00001:
        lowest = p[0]
        for i, prob in enumerate(p):
            if prob <= p[0]:
                continue
            else:
                break
            
        if prob == lowest:
            prob = 1
            i += 1
        
        if (prob - lowest) * i < u:
            for j in range(i):
                p[j] += (prob - lowest)
            u -= (prob - lowest) * i 
        else:
            for j in range(i):
                p[j] += u / i
            u = 0
            
    return np.prod(p)
    

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    u = float(input())
    p = [float(s) for s in input().split(" ")]
    
    p = np.array(p)
    p = np.sort(p)
        
    prob = answer(n, k, u, p)
    print("Case #{}: {}".format(i, prob))