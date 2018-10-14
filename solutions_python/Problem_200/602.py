# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:48:54 2017

@author: Robbe Sneyders
"""

def answer(n):
    
    previous = '0'
    
    for i, digit in enumerate(str(n)):
        
        if digit < previous:
            return answer(n - (n % 10**(len(str(n)) - i)) - 1)
            
        previous = digit
                
    return n

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, answer(n)))