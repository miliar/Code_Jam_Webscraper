#!/usr/bin/python

import sys
rl = sys.stdin.readline

def ncrmod(n,r):
    if r * 2 > n:
        r = n - r
    if r < 0 or r > n or r > 15:
        return 0
    ans = 1
    for i in range(r):
        ans = ans * (n - i)
        ans = ans / (i + 1)
    return ans % 1000

def powmod(n,k):
    if k == 0:
        return 1
    if k == 1:
        return n % 1000
    tmp = powmod(n, k / 2)
    tmp *= tmp
    tmp %= 1000
    if k % 2 == 0:
        return tmp
    return tmp * n % 1000

def isp2(k):
    return k & (k-1) == 0

def hip2(n):
    i = 2
    tot = 0
    while i <= n:
        tot += n / i
        i = i * 2
    return tot

def bad(n):
    return range(0,n+1)

def nuts(n):
    tot = 0
    for i in bad(n):
        if i % 2 == 0:
            tot += ncrmod(n,i) * powmod(3,n-i) * powmod(5,i/2)
            tot %= 1000
    return (tot * 2 + 999) % 1000

T = int(rl())
for t in xrange(1,T+1):
    n = int(rl())
    print "Case #%d: %03d" % (t,nuts(n))

