#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2017

# OversizedPancakeFlipper
# https://code.google.com/codejam/contest/3264486/dashboard#s=p0

from sys import stdin


def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))

def readstring():
    return stdin.readline().strip()

def readstrings():
    return stdin.readline().split()


sign = {'-': -1, '+': +1}

def solve(s, k):
    answer = 0
    c = 1
    n = len(s)
    f = [1] * n
    for i in range(n):
        if sign[s[i]] * c == -1:
            if i <= n - k:
                answer += 1
                c *= -1
                f[i + k - 1] = -1
            else:
                return "IMPOSSIBLE"
        c *= f[i]
    return answer


for test in range(readint()):
    tab = readstrings()
    print("Case #%i: %s"% (test+1, solve(tab[0], int(tab[1]))))


