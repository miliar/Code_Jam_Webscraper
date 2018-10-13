# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:09:14 2017

@author: David
"""

import math

def calcFunction(N, K):
    h = math.ceil(math.log(K+1, 2))
    pos = K-2**(h-1)
    N-=1
    Up = (N, 1)
    Low = (N-1, 0)
    while h>1:
        h-=1
        cntUp = 0
        cntLow = 0
        if Up[0]%2==1:
            cntUp = Up[1]
            cntLow = Up[1] + 2*Low[1]
        else:
            cntLow = Low[1]
            cntUp = Low[1] + 2*Up[1]
        Up = (math.ceil((Up[0]-2)/2), cntUp)
        Low = (math.floor((Low[0]-2)/2), cntLow)
    if pos < Up[1]:
        N = Up[0]
    else:
        N = Low[0]
    return math.ceil(N/2), math.floor(N/2)


out = open('output.txt', 'w')
t = int(input())
for el in range(1, t+1):
    N, K = input().split(' ')
    N = int(N)
    K = int(K)
    result = calcFunction(N, K)
    print("Case #" + str(el) + ": " + ' '.join([str(c) for c in result]))
    out.write("Case #" + str(el) + ": " + ' '.join([str(c) for c in result]) + "\n")
out.close()
