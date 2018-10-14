#! /usr/bin/python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

NO = 'NO'

def sum_xor(numbers):
    return reduce(lambda x,y: x ^ y, numbers, 0)

def solve(C):
    sx = sum_xor(C)
    if sx != 0:
        return NO
    else:
        s = sum(C)
        m = min(C)
        Sean = s-m
        return str(Sean)

MAX_C = 10**6

T = int(input.readline())
assert 1<=T and T<=100

for t in range(1,T+1):
    N = int(input.readline())
    assert 2<=N and N<=1000

    S = input.readline().split(' ')
    C = [int(s) for s in S]
    assert len(C)==N
    assert all(map(lambda c: 1<=c and c<=MAX_C, C))
    
    answer = solve(C)
    output.write('Case #%s: %s\n' % (t,answer))
