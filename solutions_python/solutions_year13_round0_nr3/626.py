#!/usr/bin/env python
import sys

def is_palindrom(a):
    s = str(a)
    for i in range(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def isqrt(a):
    g = (a >> a.bit_length() // 2) + 1
    res = (g + a // g) // 2
    while abs(res - g) > 1:
        g = res
        res = (g + a // g) // 2
    while res * res > a:
        res -= 1
    return res



def next_palindrom(a):
    if a < 9: return a+1
    if a == 9: return 11

    m = str(a)
    l = len(m)
    if l % 2 == 0:
        bas = m[:l/2]
        mirr = bas[::-1]
        if int(mirr) <= int(m[l/2:]):
            bas = str(int(bas) + 1)
            if len(bas) > l/2:
                mirr = bas[-2::-1]
            else:
                mirr = bas[::-1]
        return int(bas + mirr)
    else:
        bas = m[:l/2 + 1]
        mirr = bas[-2::-1]
        if int(mirr) <=int(m[l/2 + 1:]):
            bas = str(int(bas) + 1)
            if len(bas) > l/2 +1:
                bas = bas[:-1]
                mirr = bas[::-1]
            else:
                mirr = bas[-2::-1]
        return int(bas + mirr)


def howmany(l):
    a, b = (int (c) for c in l.split())

    ma = isqrt(a)
    mb = isqrt(b) + 1

    cpt = 0

    x = next_palindrom ( ma - 1 )

    while x < mb:
        y = x * x
        if is_palindrom(y):
            if a <= y <= b:
                cpt += 1
        x = next_palindrom(x)
    return cpt

if __name__ == "__main__":
    f =  open(sys.argv[1])
    exs = [ l for l in f.readlines() ]
    i = 1
    n = int(exs[0])
    while i <= n:
        print "Case #%d: %d" % (i, howmany(exs[i]))
        i += 1


