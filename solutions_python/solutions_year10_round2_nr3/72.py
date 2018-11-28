#! /usr/bin/env python
#
#   C. Your Rank is Pure
#

from __future__ import print_function

MOD = 100003

def choose(n, k):
    if k > n:
        return 0
    if k > n/2:
        k = n - k
    x = 1
    for i in xrange(1, k+1):
        x = x * (n-k+i) / i
    return x % MOD

numbers = []
for case in xrange(1, int(raw_input())+1):
    numbers.append(int(raw_input()))
maxnum = max(numbers)

t = [[0] * maxnum for i in xrange(maxnum+1)]
for n in xrange(2, maxnum+1):
    t[n][1] = 1
    t[n][n-1] = 1
for n in xrange(3, maxnum+1):
    t[n][2] = 1
    for k in xrange(3, n):
        t[n][k] = t[k][k-1]
        for i in xrange(max(1, k - (n-k)), k-1):
            t[n][k] += choose(n - k - 1, k - i - 1) * t[k][i]
            t[n][k] %= MOD

for i, num in enumerate(numbers):
    print("Case #{0}:".format(i+1), sum(t[num]) % MOD)
