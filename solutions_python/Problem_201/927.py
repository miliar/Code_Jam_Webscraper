#!/usr/bin/env python


mem = {}
def solve(N, K):
    mx = N // 2
    mn = mx if N % 2 == 1 else mx-1
    if K == 1:
        return mx, mn
    else:
        return solve(mx if K % 2 == 0 else mn, K // 2)


T = int(raw_input().strip())
for t in range(T):
    N, K = raw_input().strip().split()
    N = int(N)
    K = int(K)
    mx, mn = solve(N, K)
    print 'Case #%d: %d %d' % (t+1, mx, mn)
