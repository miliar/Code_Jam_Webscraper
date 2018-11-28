#!/bin/python

import math

caseCount = int(input())
for caseNum in range(1,caseCount+1):

    # case start
    n,k = [int(n) for n in input().split(" ")]

#    for i in range(n):
#        pancakes=[int(n) for n in input().split(" ")]

    tls=[input().split(" ") for i in range(n)]
    pancakes=[(int(r),int(h)) for (r,h) in tls]

    # sort list
    pancakes.sort(key=lambda tup: tup[0]*tup[1], reverse=True)

    maxr=0
    space=0
    # choose next values
    for i in range(k):
        (r,h) = pancakes[i]
        if r>maxr:
            maxr=r
        space+=2*r*h

    (lr,lh)=pancakes[k-1]

    for i in range(k,n):
        (r,h) = pancakes[i]
        if r>maxr:
            if 2*lr*lh+maxr*maxr<2*r*h+r*r:
                space+=2*r*h-2*lh*lr
                lr=r
                lh=h
                maxr=r

    space+= maxr*maxr

    print("Case #{}: {}".format(caseNum,math.pi*space))
    # case end
