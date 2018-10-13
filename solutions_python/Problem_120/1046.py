#!/usr/bin/env python

def compute(r, t):
    from math import sqrt, floor
    result = (1 - 2*r) + sqrt(pow(2*r - 1, 2.0) + 8.0*t)
    result = result / 4.0
    return result

def quad(a, b, c):
    from math import sqrt, floor
    d = b * b - 4.0 * a * c
    x = (-b + sqrt(d) - 0.0000000000000001) / (2*a)
    return floor(x)

if __name__ == "__main__":
    from string import split, strip
    from sys import stdin

    line = strip(stdin.readline())
    T = int(line)

    for test in range(1, T+1):
        line = strip(stdin.readline())
        [r, t] = map(lambda x: float(x), split(line))
        print "Case #%d: %d" %(test, quad(2.0, 2.0*r-1.0, -1.0*t))
