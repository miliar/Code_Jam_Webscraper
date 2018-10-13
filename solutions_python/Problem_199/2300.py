#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Name:        Google Code Jam 2017 - Qualifiers - Oversized Pancake Flipper
#
# Author:      Ashish Nitin Patil
#
# Created:     08-04-2017
# Copyright:   (c) Ashish Nitin Patil 2017
# Licence:     New BSD License
#-------------------------------------------------------------------------------

T = int(input())

for test_case in range(1, T+1):
    S, K = input().split()
    K = int(K)
    ideal = '+'*len(S)
    attempts = 0
    for i in range(len(S)-K+1):
        if S[i] != '+':
            prev = S[:i] if i > 0 else ''
            flipped = ''.join(['+' if s != '+' else '-' for s in S[i:i+K]])
            S = prev + flipped + S[i+K:]
            attempts += 1
        # print(i, attempts, S)
    answer = attempts if S == ideal else 'IMPOSSIBLE'
    print("Case #{0}: {1}".format(test_case, answer))
