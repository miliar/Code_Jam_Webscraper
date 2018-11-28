#!/usr/bin/env python3
# coding: utf-8

N = M = -1
l = []

dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

def solve():
    for x in range(N):
        for y in range(M):
            ok = [ True ] * 4
            for i in range(4):
                for j in range(max(N, M)):
                    xx, yy = x+dx[i]*j, y+dy[i]*j
                    if not (0 <= xx < N and 0 <= yy < M): break
                    if l[x][y] < l[xx][yy]: ok[i] = False
            if not ((ok[0] and ok[1]) or (ok[2] and ok[3])):
                return 'NO'
    return 'YES'

for case in range(int(input())):
    N, M = list(map(int, input().split(' ')))
    l = []
    for i in range(N): l.append(list(map(int, input().split(' '))))
    print('Case #{}: {}'.format(case+1, solve()))
