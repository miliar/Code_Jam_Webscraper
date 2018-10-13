#!/usr/bin/python

import sys
import math

def test(a):
    maxr = [0] * n
    maxc = [0] * m
    ori = [[100 for j in range(0,m)] for i in range(0,n)]
    for i in range(0,n):
        for j in range(0,m):
            maxr[i] = max(maxr[i], a[i][j])
            maxc[j] = max(maxc[j], a[i][j])
    for i in range(0,n):
        for j in range(0,m):
            if a[i][j] < maxr[i] and a[i][j] < maxc[j]:
                return False
    
       
    return True

if __name__=="__main__":
    fp=sys.stdin
    data = fp.readlines()
    N = int(data[0])
    index = 0
    case = 0
    while case < N:
        case += 1
        index += 1
        n,m = [int(x) for x in data[index].strip().split(' ')]
        board = []
        for i in range(0,n):
            index += 1
            board.append([int(x) for x in data[index].strip().split(' ')])
        res = test(board)
        print "Case #%d:" %(case),
        if res:
            print "YES"
        else:
            print "NO"

