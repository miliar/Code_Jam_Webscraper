#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    S, K = cipher.split()
    S = list(S)
    K = int(K)
    count = 0
    for i, ch in enumerate(S):
        if i+K > len(S):
            break
        if ch == '-':
            count += 1
            for j in range(K):
                S[i+j] = '-' if S[i+j] == '+' else '+'
    return count if '-' not in S else 'IMPOSSIBLE'

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
