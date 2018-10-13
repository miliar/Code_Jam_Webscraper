#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2017

# TidyNumbers
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

from sys import stdin


def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))

def readstring():
    return stdin.readline().strip()

def readstrings():
    return stdin.readline().split()


def solve(S):
    i = 0
    for j in range(1, len(S)):
        if S[j] > S[i]:
            i = j
        elif S[j] < S[i]:
            S[i] -= 1
            for k in range(i+1, len(S)):
                S[k] = 9
            break
    if S[0] == 0:
        return S[1:]
    else:
        return S


for test in range(readint()):
    S = solve(list(map(int, readstring())))
    print("Case #%i: "% (test+1), end='')
    for x in S:
        print(x, end='')
    print()


