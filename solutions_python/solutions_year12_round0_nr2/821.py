#!/bin/python

import sys

T = int(sys.stdin.readline())
for i in range(T):
    line = sys.stdin.readline().split()
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    count=0
    for j in range(N):
        if int(line[3+j])>=p+max(p-1,0)*2:
            count += 1
        elif int(line[3+j])>=p+2*max(p-2,0) and S>0:
            S -= 1
            count +=1
    print("Case #{0}: {1}".format(i+1, count))
