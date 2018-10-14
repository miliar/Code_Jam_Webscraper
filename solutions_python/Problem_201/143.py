#!/usr/bin/env python3

def solve(N, K):
    def split(x):
        return x // 2, (x-1) // 2
    L = [[N, 1]]
    i = 0
    def add(x, m):
        if L[-1][0] == x:
            L[-1][1] += m
        else:
            L.append([x, m])
    while L[i][1] < K:
        K -= L[i][1]
        distances = split(L[i][0])
        for d in distances: add(d, L[i][1])
        i += 1
    return split(L[i][0])

tests = int(input())
for test in range(tests):
    N, K = map(int, input().split())
    maxLR, minLR = solve(N, K)
    print("Case #{}: {} {}".format(1+test, maxLR, minLR))
