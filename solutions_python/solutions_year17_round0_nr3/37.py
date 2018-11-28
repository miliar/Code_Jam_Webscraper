#!/usr/bin/env python3
def solve(N, K):
    N -= 1
    m = N // 2
    M = m + (N % 2)
    if K == 1:
        return M, m
    if K % 2:
        return solve(m, K // 2)
    else:
        return solve(M, K // 2)


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    print("Case #{}: {} {}".format(t + 1, *solve(N, K)))
