#! /usr/bin/env python3


def check_lawn(lawn, N, M, rm, cm):
    for i in range(N):
        for j in range(M):
            if lawn[i][j] < rm[i] and lawn[i][j] < cm[j]:
                return "NO"
    return "YES"

T = int(input())
for case in range(T):
    lawn = []
    N, M = [int(x) for x in input().split()]
    for line in range(N):
        lawn.append([int(x) for x in input().split()])
    row_maxs = [max(row) for row in lawn]
    col_maxs = [max(row[i] for row in lawn) for i in range(M)]
    answer = check_lawn(lawn, N, M, row_maxs, col_maxs)
    print("Case #{0}: {1}".format(case + 1, answer))
