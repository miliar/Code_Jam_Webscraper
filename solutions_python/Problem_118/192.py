#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import sqrt
import sys

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]
    
DP=[]
def dp(A, B):
    i = 0
    nn = gen()
    v = 0
    while (v < A):
        i = nn.next()
        v = i ** 2
    while(v <= B):
        if is_palindrome(v):
            DP.append(v)
        i = nn.next()
        v = i ** 2

def solve(A, B):
    ans = 0
    i = 0
    max = len(DP)
    while i < max and DP[i] < A: i += 1
    while i < max and A <= DP[i] <= B:
        ans += 1
        i += 1
    return ans

def gen():
    #number size 1
    for v in [1, 2, 3]:
        yield v
    #number size 2
    for v in [11, 22]:
        yield v
    #number size 3
    for v in [101, 111, 121, 202, 212]:
        yield v
    #number size 4
    for v in [1001, 1111, 2002]:
        yield v
    #number size 5
    for v in [10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102]:
        yield v
    #number size n...
    n=6
    while True:
        if n % 2 == 0:
            #even
            exp = n / 2 - 1
            max = 2 ** exp
            for i in xrange(max):
                left = bin(2 ** exp + i)[2:]
                yield int(left + left[::-1])
            yield int('2' + (n-2) * '0' + '2')
        else:
            #odd
            for i in xrange(max):
                left = bin(2 ** exp + i)[2:]
                for middle in ['0', '1', '2']:
                    yield int(left + middle + left[::-1])
            yield int('2' + ((n-1)/2 - 1) * '0' + '0' + ((n-1)/2 - 1) * '0' + '2')
            yield int('2' + ((n-1)/2 - 1) * '0' + '1' + ((n-1)/2 - 1) * '0' + '2')
            yield int('2' + ((n-1)/2 - 1) * '0' + '2' + ((n-1)/2 - 1) * '0' + '2')
        n += 1
            
    
def palin_gen():
    max_next_value = 10
    for v in xrange(1, 10):
        yield v
    init_left_part = 0
    left_part = init_left_part
    size = 2
    while True:
        if size % 2 == 0:
            while True:
                left_part += 1
                if left_part == max_next_value:
                    left_part = init_left_part
                    size += 1
                    break
                yield int(str(left_part) + str(left_part)[::-1])
        else:
            while True:
                left_part += 1
                if left_part == max_next_value:
                    init_left_part = max_next_value - 1
                    max_next_value *= 10
                    left_part = init_left_part
                    size += 1
                    break
                for i in xrange(10):
                    yield int(str(left_part) + str(i) + str(left_part)[::-1])
    
if __name__ == '__main__':
    #print 1000
    #m=10**100
    #for _ in xrange(1000):
    #    print 1, m
    #sys.exit(0)
    dp(1, 10**100)
    #sys.exit(0)
    C = readint()
    for c in xrange(1, C+1):
        A, B = readlinearray(int)
        ans = solve(A, B)
        print 'Case #%d: %s' % (c, ans)
