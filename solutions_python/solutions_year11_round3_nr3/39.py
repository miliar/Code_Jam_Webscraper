#!/usr/bin/env python
import sys
from pylab import sqrt

def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b%a, a
    return b
def lcm(a, b):
    return a*(b/gcd(a,b))

def all_factors(n, start=2):
    i = start
    p = 0
    while i <= int(sqrt(n)):
        while (n%i==0):
            p += 1
            n /= i
        if p:
            break
        i += 1
    if p==0:
        yield 1
        if n>1:
            yield n
    else:
        for a in all_factors(n):
            b = 1
            for pp in range(p+1):
                yield b*a
                a *= i


def solve():
    N, L, H = map(int, sys.stdin.readline().split())
    f = map(int, sys.stdin.readline().split())
    f.sort()

    lc = [1]
    for i in f:
        lc.append(lcm(lc[-1], i))
    rf = reversed(f)
    gc = [rf.next()]
    for i in rf:
        gc.append(gcd(gc[-1], i))
    gc.reverse()

    # print lc
    # print gc

    ret = H+1
    for l,g in zip(lc,gc):
        if g%l != 0:
            continue
        ml = L/l + (1 if L%l!=0 else 0)
        mh = H/l
        try:
            mm = min(m for m in all_factors(g/l) if ml<=m<=mh)
            ret = min(ret, mm*l)
        except ValueError:      # empty list
            pass

    l = lc[-1]
    ml = L/l + (1 if L%l!=0 else 0)
    mh = H/l
    if ml<=mh:
        ret = min(ret, l*ml)

    if ret<H+1:
        return ret
    else:
        return 'NO'

        
        


if __name__=="__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        print "Case #{}: {}".format(t+1, solve())

