# -*- coding: utf-8 -*-
import sys

def gcd(a, b):
    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    return gcd(b % a, a)
        

fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    t = map(int, fin.readline().split())[1:]
    m = t[0]
    last = 0
    for k in t:
        last = gcd(last, abs(k-m))
    print "Case #%d: %s" % (case,  (- m) % last)
