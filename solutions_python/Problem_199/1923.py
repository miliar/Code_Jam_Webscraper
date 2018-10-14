#!/usr/bin/env python

import os
import sys

def invert(s):
    return '-' if s == '+' else '+'

def flip(S, K, i):
    return S[:i] + ''.join(map(invert, S[i:i + K])) + S[i + K:]

def solve(S, K):
    s = '+' * len(S)
    k = '+' * K
    seen = set([S])
    queue = [(S, 0)]
    while queue:
        S, N = queue.pop(0)
        if S == s:
            return N
        for i in range(len(S) - K + 1):
            if S[i:i+K] == k:
                continue
            SS = flip(S, K, i)
            if SS in seen:
                continue
            seen.add(SS)
            queue.append((SS, N + 1))
    return None

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        S, K = sys.stdin.readline().strip().split()
        K = int(K)
        result = solve(S, K)
        if result is None:
            print 'Case #%d: IMPOSSIBLE' % (t + 1)
        else:
            print 'Case #%d: %d' % (t + 1, result)

if __name__ == '__main__':
    main()

