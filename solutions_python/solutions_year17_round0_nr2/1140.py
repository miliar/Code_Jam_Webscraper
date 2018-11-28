# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:30:05 2017

@author: Özcan
"""

def check(n):
    mindigit = 9
    while n>0:
        digit = n % 10
        n = n // 10
        if digit <= mindigit:
            mindigit = digit
        else:
            return False
    return True

def solve(N):
    if check(N) == True:
        return N
    
    while True:
        # convert to string for easier comparison
        Nstr = str(N)
        
        # find first problematic position
        for i in range(len(Nstr)-1):
            if int(Nstr[i]) > int(Nstr[i+1]):
                break
        new_nstr = Nstr[:i+1] + '0'*len(Nstr[i+1:])
        new_N = int(new_nstr) -1
        if check(new_N) == True:
            return new_N
        N = new_N

numberCases = int(input())

for i in range(1,numberCases+1):
    N = int(input())
    result = solve(N)
    print("Case #{}: {}".format(i, result))