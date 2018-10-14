#!/bin/python

import sys

T = int(sys.stdin.readline())
for i in range(T):
    line = sys.stdin.readline().split()
    A = int(line[0])
    B = int(line[1])
    count = 0
    for j in range(A,B):
        s = str(j)
        l = []
        for k in range(1,len(s)):
            a = int(s[k:]+s[:k])
            if a > j and a <= B and a not in l:
                l += [a]
                count += 1
    print("Case #{0}: {1}".format(i+1, count))
