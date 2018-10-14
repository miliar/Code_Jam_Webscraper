#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
def gcd(a, b):
    r = a % b
    if r:
        return gcd(b, r)
    else:
        return b

def lcm(a, b):
    return a * b / gcd(a, b)

def lcmAll(seq):
    return reduce(lcm, seq)


def solve(m, n):
    lcm = lcmAll(m)
    circle = sum([lcm/x for x in m])
    n = n % circle
    if n == 0:
        n = circle

    # print 'circle', circle, 'n',n 
    b = len(m)
    r = [[0, i] for i in xrange(b)]
    while n > 0:
        r.sort(reverse=True)
        # print 'r', r
        index = r[-1][1]
        r[-1][0] += m[index]
        n -= 1
    return index+1

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
def test():
    assert gcd(8, 6) == 2
    assert gcd(8, 4) == 4
    assert lcm(8, 6) == 24
    assert lcmAll((8, 6, 4)) == 24
    assert lcmAll((8, 6, 5)) == 120

    sp([10, 5], 4, 1)
    sp([7,7,7], 12, 3)
    sp([4,2,1], 8, 1)
    sp([1,1,1], 1, 1)
    sp([1,1,1], 2, 2)
    sp([1,1,1], 3, 3)
    sp([1,1,1], 4, 1)
    pass

def readInt():
    return int(sys.stdin.readline().strip())
    
def readInts():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def readStrs():
    return [x for x in sys.stdin.readline().strip().split()]

def main():
    n = readInt()
    for i in xrange(n):
        b, n = readInts()
        m= readInts()
        print 'Case #%d: %s' % (i+1, solve(m, n))
    pass

if __name__ == '__main__':
    main()