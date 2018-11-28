#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import math

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in raw_input().split()]
def readint(): return int(raw_input().strip())

debug = lambda x: x

def mark_primes(n):
    nums = range(n+1)
    nums[1] = 0
    for num in nums:
        if num == 0:
            continue
        for multiple in xrange(num*2, n+1, num):
            nums[multiple] = 0
    return nums

def calc(N):
    if N == 1:
        return 0

    min_count = 0
    max_count = 1
    primes = (num for num in mark_primes(1000) if not num == 0)
    for p in primes:
        if p <= N:
            m = int(math.log(N, p))
            min_count += 1
            debug(p)
            debug(m)
            max_count += m
        else:
            break
    return max_count - min_count

T = readint()
for i in xrange(1, T+1):
    N = readint()
    print('Case #{0}: {1}'.format(i, calc(N)))

