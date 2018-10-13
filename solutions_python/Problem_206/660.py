#!/usr/bin/env python
from math import *
from sys import *

numcases = int(stdin.readline())

for case in range(1,numcases+1):
    nums = stdin.readline().split()
    D = float(nums[0])
    N = int(nums[1])
    otherhorses = []
    for i in range(N):
        otherhorses.append(map(float,stdin.readline().strip().split()))

    maxT = 0
    for horse in otherhorses:
        t = (D-horse[0])/horse[1]
        maxT = max(maxT,t)

    speed = D/maxT



    print "Case #" + str(case) + ": " + str(speed)


