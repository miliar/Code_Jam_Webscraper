#!/usr/bin/env python

def solve(N, K):
    if K == N: return (0, 0)
    if K == 1: return (N // 2, (N - 1) // 2)

    if (K - 1) % 2:
        return solve(N // 2, K // 2)
    else:
        return solve((N - 1) // 2, (K - 1) // 2)

T = int(input().strip())
for t in range(T):
    N, K = map(int, input().strip().split())
    
    y, z = solve(N, K)
    print ('Case #%d: %d %d' % (t + 1, y, z))
