#!/usr/bin/python

import sys

data = file(sys.argv[1]).read().splitlines()

T = int(data.pop(0))

def bruterev(M):
    ss = '%d' % M
    s = ss[::-1].lstrip('0')
    return int(s)

def rev(M):
    while M % 10 == 0:
        M = M / 10
    m = 0
    while M:
        m = (m * 10) + (M % 10)
        M = M / 10
#        print M, m, (M % 10)
#    print m
    return m

if False:
    for i in xrange(1,100000):
        print i, rev(i), rev(i) - i
    assert False

def brute(N):
    c = 1
    n = 1
#    print 'trying', N
    while c < N:
        r = rev(c)
#        assert r == bruterev(c)
        if r > c + 1 and r <= N:
            c = r
        else:
            c = c + 1
        n = n + 1
#        print c, r, n
    return n

def brute2(X):
    if X % 10:
        return min(brute(X), brute(rev(X)) + 1)
    else:
        return brute(X)

def brute3(N):
    CACHE = [ 10**6 for x in xrange(0,N+1)]
    CACHE[N]=1
    n = N - 1
#    print n
    while n:
        r = rev(n)
#        print 'n is',n
        if r > n and r <= N:
            CACHE[n] = min(CACHE[n+1] + 1,CACHE[r] + 1)
        else:
            CACHE[n] = CACHE[n+1] + 1
        n = n - 1
    return CACHE[1]

for CASE in xrange(1,T+1):
    print 'Case #%d:' % (CASE),
    N = int(data.pop(0))
    print brute3(N)


