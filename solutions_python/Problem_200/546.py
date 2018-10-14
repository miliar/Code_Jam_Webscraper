# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:54:44 2017

@author: Miguel
"""

import sys

def isTidyNumber(n):
    n = str(n)
    size = len(n)
    for i in range(1, size):
        if int(n[size-i]) < int(n[size - (i+1)]):
            return False
    return True
        
def fasterDecrease(n):
    n = str(n)
    for i in range(0, len(n)-1):
        if int(n[i] > n[i+1]):
            break
    aux = int(n[i+1:]) + 1
    #print aux + 1
    #if aux == 0:
    #    aux = 1
    return int(n) - aux

def findTidyNumber(n):
    while True:
        if isTidyNumber(n):
            return n
        n = fasterDecrease(n)
        #n = n - 1


counter = 0

for line in sys.stdin:
    if counter == 0:
        counter += 1
        n_cases = int(line)
        continue
    n = int(line)
    print "Case #" + str(counter) + ": " + str(findTidyNumber(n))
    counter += 1