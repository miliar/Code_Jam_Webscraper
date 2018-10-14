# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:03:51 2017

@author: Robbe Sneyders
"""

def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

def answer(n, m):
    
    d = {n:1}
    
    while m > 0:
        maxi = max(d, key=int)
        
        new = (maxi - 1) // 2
        
        if maxi % 2 == 1:
            d[new] = d.get(new, 0) + d[maxi] * 2
        else:
            d[new] = d.get(new, 0) + d[maxi]
            d[new + 1] = d.get(new + 1, 0) + d[maxi]
        
        m -= d[maxi]
                
        del d[maxi]
    
    if maxi % 2 == 1:   
        return(new, new)
    else:
        return(new + 1, new)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    y, z = answer(n, m)
    print("Case #{}: {} {}".format(i, y, z))