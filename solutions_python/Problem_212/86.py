#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2017

# FreshChocolate
# https://code.google.com/codejam/contest/dashboard?c=5314486#s=p0

from sys import stdin


def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))

def readstring():
    return stdin.readline().strip()

def readstrings():
    return stdin.readline().split()


def solve(p, g):
    n = [0] * p
    for x in g:
        n[x % p] += 1
    answer = n[0]
    if p == 2:
        answer += (n[1] + 1 ) // 2
    elif p == 3:
        answer += min(n[1], n[2])
        k = max(n[1], n[2]) - min(n[1], n[2])
        answer += (k + 2) // 3
    elif p == 4:
        answer += min(n[1], n[3])
        answer += n[2] // 2
        if n[1] != n[3] or (n[2] % 2) == 1:
            answer += 1
    return answer


for test in range(readint()):
    n, p = readints()                 # read input
    g = readints()
    print("Case #%i: %i"% (test+1, solve(p, g)))
