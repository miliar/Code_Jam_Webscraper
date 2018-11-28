#!/usr/bin/python
import math

def guessN(m, t):
    b = m - 2
    delta = b * b - 8 * t
    if delta < 0:
        delta = -delta
    delta = math.sqrt(delta)
    return int(abs((delta - b) / 4))

def calcSum(m, n):
    return (m + m + (n - 1) * 4) * n / 2

def solve(r, t):
    m = (r + 1) * (r + 1) - r * r
    n = guessN(m, t)
    nsum = calcSum(m, n)
    if nsum == t:
        return n
    elif nsum > t:
        while True:
            n -= 1
            nsum = calcSum(m, n)
            if nsum <= t:
                break
    else:  # nsum < t
        while True:
            n += 1
            nsum = calcSum(m, n)
            if nsum > t:
                break
        n -= 1
    return n

if __name__ == "__main__":
    cases = int(raw_input())
    for testCase in xrange(1, cases + 1):
        line = raw_input().split(" ")
        r, t = int(line[0]), int(line[1])
        # print "r = %d, t = %d" % (r, t)
        print "Case #%d: %d" % (testCase, solve(r, t))
