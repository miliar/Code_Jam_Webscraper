#!/usr/bin/env python3

def solve(D, N, K, S):
    return D / max(float(D-K[i])/S[i] for i in range(N))

tests = int(input())
for test in range(tests):
    D, N = map(int, input().split())
    K = []
    S = []
    for i in range(N):
        k, s = map(int, input().split())
        K.append(k)
        S.append(s)
    result = solve(D, N, K, S)
    print("Case #{}: {:0.6f}".format(1+test, result))
