from __future__ import division
"""
Code Jam 2011
Round1C: Problem c
"""
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcdm(*args):
    return reduce(gcd, args)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)

def compute(l, h, freqs):
    def ismultiple(a, b):
        if a >= b and a % b == 0: return True
        if b > a and b % a == 0: return True
        return False

    for f in range(l, h + 1):
        if all([ismultiple(f, n) for n in freqs]):
            return f
    return "NO"

def main():
    num_tests = int(sys.stdin.readline())
    for t in range(1, num_tests + 1):
        n, l, h = [int(x) for x in sys.stdin.readline().split()]
        freqs = [int(x) for x in sys.stdin.readline().split()]
        assert len(freqs) == n
        result = compute(l, h, freqs)
        print "Case #%d: %s" % (t, result)

if __name__ == '__main__':
    main()
