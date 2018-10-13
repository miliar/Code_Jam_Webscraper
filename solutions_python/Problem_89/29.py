import sys
from fractions import gcd
import numpy as np
from math import log

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'test.in'

    with open(filename) as f:
        numCases = int(f.readline())
        for caseNo in xrange(1, numCases+1):
            N = int(f.readline())
            ans = solve(N)
            print 'Case #{0}: {1}'.format(caseNo, ans)

def sieve(n, mn=0):
    is_prime = np.ones(n+1, bool)
    primes = []
    for test in xrange(2, n+1):
        if is_prime[test]:
            if test > mn:
                primes.append(test)
            is_prime[0::test] = False
    return primes

def solve(N):
    if N == 1:
        return 0
    primes = sieve(N)
    best = len(primes)
    worst = 1
    for p in primes:
        worst += int(log(N, p))
    return worst - best


if __name__ == '__main__':
    main()
