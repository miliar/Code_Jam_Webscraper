#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2017

# Stable-Neigh-bors
# https://code.google.com/codejam/contest/8294486/dashboard#s=p1


from sys import stdin
from pprint import PrettyPrinter
from math import floor, ceil

pp = PrettyPrinter()

def readint():
    return int(stdin.readline())

def readints():
    return tuple(map(int, stdin.readline().split()))

def readstring():
    return stdin.readline().strip()

def readstrings():
    return stdin.readline().split()


def div_round_up(x, y):
    if x % y == 0:
        return x // y
    else:
        return (x // y) + 1


def solve(n, R, O, Y, G, B, V):
    """complexity: O(n) - but in fact n^2 because of string append
    """
    S = "RBYGOV"
    # _,i = max((T[i], i) for i in range(3))
    for k in range(3):
        T = [R, B, Y, G, O, V]
        i = k
        s = ""
        for _ in range(n):
            s += S[i]
            T[i] -= 1
            if i >= 3:
                i -= 3
            else:
                if T[i+3] > 0:
                    i += 3
                else:
                    _, i = max((T[j],j) for j in range(3) if j != i)
                    # if T[(i + 1)%3] >= T[(i+2)%3]:
                    #     i = (i+1)%3
                    # else:
                    #     i = (i+2)%3
        if (s[0] != s[-1] and min(T) == 0):
            return s
    return("IMPOSSIBLE")


for test in range(readint()):
    n, R, O, Y, G, B, V = readints()
    print("Case #%i: %s" % (test+1, solve(n, R, O, Y, G, B, V)))


