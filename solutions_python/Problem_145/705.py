#!python2
from __future__ import division, print_function

import sys
from pprint import pprint as pp

def is_power2(num):
    '''only for integers'''
    return ((num & (num - 1)) == 0) and num != 0

def log2(num):
    '''only for integers'''
    return len(bin(num)) - 3

def reduce_(p, q):
    '''Reduces to lowest terms
    return (p', n) if p/q = p'/2^n, otherways returns None'''
    a = p
    b = q
    while (b % 2 == 0) and (a % 2 == 0):
        a = a//2
        b = b//2

    if b % a == 0:
        b = b//a
        a = 1

    if is_power2(b):
        return a, log2(b)
    else:
        return None

def reduce2(p, n):
    assert(p <= 2**n)
    while (p % 2 == 0) and (n > 0):
        p = p//2
        n = n-1
    return p, n

def min_generations(p, n):
    'One has p/2^n elf blood. how far is the closet possible Elf ancestor?'
    assert(p <= 2**n)

    p, n = reduce2(p, n)

    if n == 0: # (1/1), I have found the elf ancestor
        assert(p == 1)
        return 0

    if p == 1:
        # one parent has 0, the other 1/2^(n-1)
        return 1 + min_generations(p, n-1)

    return 1 + min_generations(2**log2(p), n-1)

def result(p, q):
    #print((p, q), file=sys.stderr)
    try:
        p, n = reduce_(p, q)
    except TypeError:
        return 'impossible'
    #print((p, 2**n), file=sys.stderr)
    if n > 40:
        return 'impossible'

    return min_generations(p, n)

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        p, q = (int(x) for x in sys.stdin.readline().strip().split('/'))
        print("Case #{}: {}".format(str(t+1), result(p, q)))
