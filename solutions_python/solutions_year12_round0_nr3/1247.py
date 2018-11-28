#!/usr/bin/env python

def recycle(n):
    digits = []
    ret = []
    while n:
        digits.append(n%10)
        n /= 10
    digits.reverse()
    k = 0
    l = len(digits)
    i = 1
    while i < l:
        m,d,k = 0,0,i
        while d < l:
            d += 1
            m = m*10 + digits[k]
            k = (k + 1) % l
        ret.append(m)
        i += 1
    return ret

T = int(raw_input())
for t in range(T):
    A, B = [int(x) for x in raw_input().split()]
    count = 0
    for n in range(A,B+1):
        l = recycle(n)
        for m in l:
            if n < m <= B:
                count += 1
    print 'Case #%d: %d' % (t+1,count)
