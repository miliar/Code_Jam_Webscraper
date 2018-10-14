# -*- coding: utf-8 -*-

def fact(n):
    ret = {}
    m = 2
    while m * m <= n:
        if n % m == 0:
            ret[m] = ret.get(m, 0) + 1
            n /= m
        else:
            m += 1
    if n != 1:
        ret[n] = ret.get(n, 0) + 1
    return ret

T = int(raw_input())
for case in xrange(1, T + 1):
    N, L, H = map(int, raw_input().split(' '))
    F = map(int, raw_input().split(' '))

    for n in xrange(L, H + 1):
        ng = False
        for i in xrange(N):
            if n % F[i] != 0 and F[i] % n != 0:
                ng = True
                break
        if not ng:
            print 'Case #%d: %d' % (case, n)
            break
    else:
        print 'Case #%d: NO' % case

