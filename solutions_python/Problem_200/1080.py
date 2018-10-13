#!/usr/bin/env python


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for i in range(1, t+1):
    num = int(inFile.readline())
    inStr = str(num)
    inList = [int(x) for x in inStr]
    n = len(inStr)
    marker = None
    for x in range(1, n):
        if(inList[-x] < inList[-x-1]):
            inList[-x] = 9
            inList[-x-1] -= 1
            marker = n-x
    inStr = ''
    for x in inList:
        inStr += str(x)
    if(marker is not None):
        inStr = inStr[:marker] + '9'*len(inStr[marker:])
    ans = int(inStr)
    outFile.write("Case #{}: {}\n".format(i, ans))
