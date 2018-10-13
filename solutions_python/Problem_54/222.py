#!/usr/bin/env python

import fileinput
import math

def main():
    reader = fileinput.input()
    n = int(reader.next())
    for case in range(1, n+1):
        a = [long(w) for w in reader.next().strip().split()]
        print "Case #%d: %s" % (case, warning(*a))

def gcd(a, b):
    while a != 0 and b != 0:
        if a < b:
            b = b % a
        else:
            a = a % b
    if a == 0:
        return b
    else:
        return a

def warning(n, *a):
    m = abs(a[1] - a[0])
    for k in range(1, n - 1):
        m = gcd(m, abs(a[k + 1] - a[k]))
    r = a[0] % m
    if r == 0:
        return 0
    else:
        return m - r

main()
