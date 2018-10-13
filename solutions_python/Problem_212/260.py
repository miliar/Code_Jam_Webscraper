#!/usr/bin/env python
import numpy as np


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for test in range(1, t+1):
    N, P = map(int, inFile.readline().split(' '))
    groups = map(int, inFile.readline().split(' '))
    moddedGroups = [x % P for x in groups]
    ans = 0
    # print moddedGroups
    if(P == 2):
        ans += moddedGroups.count(0)
        temp = moddedGroups.count(1)
        ans += temp/2
        if(temp % 2 == 1):
            ans += 1
    elif(P == 3):
        ans += moddedGroups.count(0)
        temp1 = moddedGroups.count(1)
        temp2 = moddedGroups.count(2)
        ans += min(temp1, temp2)
        temp1 = max(temp1, temp2) - min(temp1, temp2)
        ans += temp1/3
        if(temp1 % 3 != 0):
            ans += 1
    else:
        ans += moddedGroups.count(0)
        n2s = moddedGroups.count(2)
        ans += n2s/2
        n1s = moddedGroups.count(1)
        n3s = moddedGroups.count(3)
        ans += min(n1s, n3s)
        r2s = 0
        if(n2s % 2 == 1):
            r2s = 1
        rs = max(n1s, n3s) - min(n1s, n3s)
        if(rs >= 2 and r2s):
            ans += 1
            r2s -= 1
            rs -= 2
        ans += rs/4
        rs = rs - rs/4
        if(rs or r2s):
            ans += 1
    outFile.write("Case #{}: {}\n".format(test, ans))
    # print ans
