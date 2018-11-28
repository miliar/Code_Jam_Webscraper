# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 12:25:37 2017

@author: pdossantos
"""

import sys, numpy

name = "B-large"
path = r""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    n = int(input())
    tidy = False
    while tidy != True:
        start = n
        ndigits = [int(x) for x in str(n)]
        diff = numpy.diff(ndigits)
        if len(diff) > 0:
            idxs = numpy.where(diff<0)[0].tolist()
            if len(idxs) > 0:
                idx = idxs[0] + 1
                start = int(''.join(str(x) for x in ndigits[:idx]) + "0" * len(ndigits[idx:]))
        for num in reversed(range(start+1)):
            start_digits = [int(x) for x in str(num)]
            tidy = all(start_digits[i+1] - start_digits[i] >= 0 for i in range(0, len(start_digits) - 1))
            if num == int(start) - 9:
                n = num
                break
            if tidy == True:
                print("Case #" + str(testCase) + ": " + str(num))
                break
            
    
            
            
            
            
            
