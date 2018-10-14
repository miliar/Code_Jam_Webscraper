#!/usr/bin/env python
import sys


def swap_sides(x, l, K):
    for i in range(l, l + K):
        x[i] = {'+': '-', '-': '+'}[x[i]]
    return x


def solve(S, K):
    i = 0
    L = len(S)
    result = 0
    while True:
        while (i < L and S[i] == '+'):
            i+= 1
        if i == L:
            return result
        if i + K > L:
            return "IMPOSSIBLE"
        swap_sides(S, i, K)
        result+= 1


if __name__ == '__main__':
    sys.stdin.readline()
    for num, line in enumerate(sys.stdin, 1):
        S, K = line.strip().split()
        S = list(S)
        K = int(K)
        print "Case #{0}: {1}".format(num, solve(S, K))
