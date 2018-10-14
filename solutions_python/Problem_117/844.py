#!/usr/bin/python3

import sys

def case():
    N, M = [int(x) for x in sys.stdin.readline().split()]
    field = []
    for i in range(0, N):
        field.append([int(x) for x in sys.stdin.readline().split()])
    for i in range(0, N):
        for j in range(0, M):
            mx = 0
            for k in range(0,M):
                if k == j: continue
                mx = max(mx, field[i][k])
            my = 0
            for k in range(0, N):
                if k == i: continue
                my = max(my, field[k][j])
            if field[i][j] < mx and field[i][j] < my: return "NO"
    return "YES"

T = int(sys.stdin.readline())
for i in range(1,T+1):
    print("Case #%s: %s" % (i, case()))
    

