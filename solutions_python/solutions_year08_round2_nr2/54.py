#!/usr/bin/env python

import sys
import os

import psyco
psyco.full()

from random import shuffle

def atkin(limit):
    """Calculates all prime numbers up to limit using the sieve of Atkin."""
    results = [2, 3]
    root = int(limit**0.5)+1
    sieve = [False]*limit
    
    for x in range(1, root):
        for y in range(1, root):
            n = 4*(x**2)+y**2
            if n < limit and n % 12 in (1,5):
                sieve[n] = not sieve[n]
            n = 3*(x**2)+y**2
            if n < limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3*(x**2)-y**2
            if (x > y) and n < limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for i in range(5, root):
        if sieve[i]:
            square = i**2
            tmp = square
            while tmp < limit:
                sieve[tmp] = False
                tmp += square

    for i, v in enumerate(sieve):
        if v:
            results.append(i)

    return results

def share_prime_factor(a,b, primes):
    for prime in primes:
        if a%prime == 0 and b % prime == 0:
            return True
    return False

def share_primes(a,b, primes):
    for na in a:
        for nb in b:
            if share_prime_factor(na, nb, primes):
                return True
    return False


def check_primes(sets, primes):
    shuffle(sets)
    for i, a in enumerate(sets[:-1]):
        for j, b in enumerate(sets[i+1:]):
            if share_primes(a,b, primes):
                return i, j+i+1
    return None
def run_case(handle):
    values = map(int, handle.readline().strip().split())

    a, b, p = values
    
    numbers = range(a,b+1)
    sets = []

    primes = atkin(b)
    primes = filter(lambda x: x >= p, primes)
    for i in numbers:
        sets.append([i])

    sets = sets[::-1]
    while True:
        try:
            i, j = check_primes(sets, primes)
            a = sets[i]
            b = sets.pop(j)
            a.extend(b)
        except TypeError:
            break
    return len(sets)

def main():
    handle = open(sys.argv[1])

    testcases = int(handle.readline())
    for i in range(testcases):
        print "Case #%d: %d" % (i+1, run_case(handle))

if __name__ == '__main__':
    main()
