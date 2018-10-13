#!/usr/bin/env python3
# -*- coding: utf-8 -*-

change = {
    '-': '+',
    '+': '-'}


def flip(S, i, k):
    prev = S[:i]
    post = S[i + k:]
    todo = S[i:i + k]
    new = ''.join([change[s] for s in todo])
    return ''.join([prev, new, post])


T = int(input())  # number of test cases
for t in range(T):
    S, K = input().split()
    K = int(K)

    # print(S)
    flips = 0
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            # flip with this as the leftmost
            S = flip(S, i, K)
            # print(S)
            flips += 1

    # recheck
    good = True
    for s in S:
        if s == '-':
            good = False
            break
    if good:
        print("Case #{:d}: {}".format(t + 1, flips))
    else:
        print("Case #{:d}: {}".format(t + 1, 'IMPOSSIBLE'))
