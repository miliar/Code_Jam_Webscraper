#!/usr/bin/env python3

def solve(S, K):
    n = len(S)

    flips = 0

    for i in range(n-K+1):
        if not S[i]:
            S[i:i+K] = [not x for x in S[i:i+K]]
            flips += 1

    if False in S:
        return "IMPOSSIBLE"

    return flips

T = int(input())
for i in range(T):
    S, K = input().split()
    S = [True if c == '+' else False for c in S]
    K = int(K)
    result = solve(S, K)
    print(f'Case #{i+1}: {result}')
