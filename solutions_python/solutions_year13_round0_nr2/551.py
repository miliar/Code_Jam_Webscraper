#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin, stdout

def rotate(n, m, lawn):
    new_lawn = [[None]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            new_lawn[j][i] = lawn[i][j]
    return new_lawn

def solve(n, m, lawn):
    new_lawn = [[100]*m for i in range(n)]
    for i in range(2):
        for (j, row) in enumerate(lawn):
            h = max(row)
            new_lawn[j] = [min(h, new_lawn[j][k]) for k in range(m)]
        lawn = rotate(n, m, lawn)
        new_lawn = rotate(n, m, new_lawn)
        (n, m) = (m, n)
    return lawn == new_lawn

if __name__ == "__main__":
    t = int(stdin.readline())
    for i in range(t):
        (n, m) = map(int, stdin.readline().strip().split())
        lawn = [map(int, stdin.readline().strip().split()) for j in range(n)]
        print("Case #{0}: {1}".format(i+1, "YES" if solve(n, m, lawn) else "NO"))
