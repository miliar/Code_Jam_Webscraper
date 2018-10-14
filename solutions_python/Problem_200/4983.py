# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 23:28:02 2017

@author: Yeou
"""

def isTidy(x):
    """
    A tidy number is one that is sorted in non-decreasing order
    Args: x, integer >=1
    Returns: True if x is tidy, False otherwise.
    """
    strx = list(str(x))
    numList = [int(i) for i in strx]
    for i in range(1, len(numList)):
        if numList[i-1] > numList[i]:
            return False
    return True
    
T = int(input(""))
for i in range(T):
    N = int(input(""))
    temp = 0
    for j in range(1,N+1):
        if isTidy(j) == True:
            temp = j
    print("Case #" + str(i+1) + ": " + str(temp))