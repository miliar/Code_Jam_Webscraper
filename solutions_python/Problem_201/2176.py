#!/usr/bin/env python3

import math

def maxAvailableSpace(nSpace, nPeople):
    return math.ceil((nSpace - nPeople + 1)/2**int(math.log(nPeople,2)))

t = int(input()) 
for i in range(1, t + 1):
    nSpace,nPeople =  [int(s) for s in input().split(" ")] 
    maxSpace = math.ceil((maxAvailableSpace(nSpace,nPeople)- 1)/2.0)
    minSpace = math.floor((maxAvailableSpace(nSpace,nPeople)-1)/2.0)    
    print("Case #{}: {} {}".format(i, maxSpace, minSpace))