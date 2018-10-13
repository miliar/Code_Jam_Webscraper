#-------------------------------------------------------------------------------
# Name:        ??????1
# Purpose:
#
# Author:      myegor
#
# Created:     21.05.2011
# Copyright:   (c) myegor 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

input = open('data1.txt','r')

testnum = int(input.readline())

for i in range(testnum):
    N =  int(input.readline())
    arr = []
    for k in range(N):
        arr.append(input.readline())

    WP = []
    for k in range(N):
        WP.append(0.0)
        won = 0.0;
        e = 0.0
        for z in range(len(arr[k])):
            if arr[k][z] == '1':
                won += 1
            if  arr[k][z] == '0':
                e += 1
        WP[-1] = won / (won+e)

    OWP = []
    for k in range(N):
        OWP.append(0.0)
        p = 0
        for z in range(N):
            if z == k:
                continue
            if arr[z][k] == '.':
                continue
            p += 1
            won = 0.0
            e = 0.0
            for y in range(len(arr[z])):
                if arr[z][y] == '1' and y != k:
                    won += 1
                if arr[z][y] == '0' and y != k:
                    e += 1
            OWP[-1] += won / (won+e)
        if p != 0:
            OWP[-1] /= p

    OOWP = []

    for k in range(N):
        OOWP.append(0.0)
        p = 0
        for z in range(N):
            if z == k:
                continue
            if arr[z][k] == '.':
                continue
            p += 1
            OOWP[-1] += OWP[z]
        if p != 0:
            OOWP[-1] /= p

    print "Case #"+str(i+1)+":"
    for k in range(N):
        print WP[k]*0.25 + 0.5 * OWP[k] + 0.25*OOWP[k]




input.close()
