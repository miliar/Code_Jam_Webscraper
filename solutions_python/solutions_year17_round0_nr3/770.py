#!/usr/bin/env python3
def solve(n, k):
    if n == k:
        return (0, 0)
    n -= 1
    k -= 1
    n_l = n // 2
    n_r = n - n_l
    k_l = k // 2
    k_r = k - k_l
    if k == 0:
        return (n_r, n_l)
    if k == 1:
        return solve(n_r, 1)
    if n % 2 == 1 and k % 2 == 0:
        return solve(n_l, k_l)
    else:
        return solve(n_r, k_r)

t = int(input())
for i in range(1, t+1):
    n, k = [int(s) for s in input().split()]
    y, z = solve(n, k)
    print('Case #{}: {} {}'.format(i, y, z))
