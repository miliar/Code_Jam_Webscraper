#!/usr/bin/python
# coding: utf8

"""
    Google Code Jam 2017 - Qualification round
    Problem A
"""

from sys import stdin


def flip(s, i, k):
    for x in range(i, i + k):
        if s[x] == '-':
            s[x] = '+'
        else:
            s[x] = '-'
    return s


def solve():
    case = stdin.readline()
    dataset = case.split()
    row = [c for c in dataset[0]]
    k = int(dataset[1])
    if '-' not in row:
        return 0
    f = 0
    i = 0
    while row:
        if row[0] == '+':
            row = row[1:]
        else:
            if k > len(row):
                return 'IMPOSSIBLE'
            elif '+' not in row[0:k]:
                row = row[k:]
                f += 1
            else:
                for j in range(k):
                    if row[j] == '+':
                        if j + k > len(row):
                            return 'IMPOSSIBLE'
                        row = flip(row, j, k)
                        f += 1
                        break
    return f

if __name__ == '__main__':
    n = int(stdin.readline())
    for i in range(n):
        print('Case #%i: %s' % (i + 1, solve()))
