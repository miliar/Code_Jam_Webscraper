#!/usr/bin/python3

import sys

def getrow(n):
    ret = []
    for j in range(4):
        row = [int(x) for x in sys.stdin.readline().split()]
        if j+1 == n: ret = row
    return ret

t = int(sys.stdin.readline())
for i in range(t):
    first = int(sys.stdin.readline())
    fnum = getrow(first)
    second = int(sys.stdin.readline())
    snum = getrow(second)
    cornum = -1
    for num in fnum:
        if num in snum:
            if cornum == -1: cornum = num
            else: cornum = -2
    print("Case #" + str(i+1) + ": ", end="")
    if cornum == -1:
        print("Volunteer cheated!")
    elif cornum == -2:
        print("Bad magician!")
    else:
        print(cornum)
                

    