#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def solve(cipher):
    Ss, K = cipher.split(" ")
    K = int(K)
    S = [0 if s=='-' else 1 for s in Ss]

    value = 0
    for idx in range(0, len(S)-K+1, 1):
        if 0 == S[idx]:
            value += 1
            for s in range(idx, idx+K, 1):
                S[s] = 0 if S[s] == 1 else 1

    if 0 != S.count(0):
        return "IMPOSSIBLE"
    else:
        return str(value)

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
