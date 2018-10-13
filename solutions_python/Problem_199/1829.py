#!/usr/bin/env python
# encoding: utf-8

'''
oversized_pancake_flipper.py
Created by Shuailong on 2017-04-08.
https://code.google.com/codejam/contest/3264486/dashboard
'''

T = int(raw_input())
for case in xrange(1, T + 1):
    S, K = raw_input().split(" ")
    S = list(S)
    K = int(K)
    result = ''
    flips = 0
    for i in range(len(S)-K+1):
        if S[i] == '+':
            continue
        else:
            flips += 1
            for j in range(i, i+K):
                if S[j] == '+':
                    S[j] = '-'
                else:
                    S[j] = '+'
    for i in range(len(S)-K+1, len(S)):
        if S[i] == '-':
            result = 'IMPOSSIBLE'
            break
    if result != 'IMPOSSIBLE':
        result = flips

    print "Case #{}: {}".format(case, result)
