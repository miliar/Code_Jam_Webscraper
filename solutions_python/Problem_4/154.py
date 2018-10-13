#!/usr/bin/env python
"minimum scalar product"
import sys

def read_vector():
    s = sys.stdin.readline().strip()
    return [int(x) for x in s.split()]

def scalar_prod(v1, v2):
    prod = 0
    for i in xrange(len(v1)):
        prod += v1[i] * v2[i]
    return prod


def minimum_scalar_product():
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        vector1 = read_vector()
        vector2 = read_vector()
        assert(len(vector1) == len(vector2))
        assert(len(vector1) == N)

        vector1.sort()
        vector2.sort(reverse=True)
        prod = scalar_prod(vector1, vector2)
        print 'Case #%d: %d' % (t+1, prod)
    if False: print t

if __name__ == "__main__":
    minimum_scalar_product()
