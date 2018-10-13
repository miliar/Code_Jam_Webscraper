#!/usr/bin/python

import sys
import math

try:
  import psyco
  psyco.full()
except Exception, e:
  pass

###

def sieveOfErat(end):
    """ Let's use the simpler Sieve of Eratostenes
        Code from: http://krenzel.info/?p=83
        Note that using psyco (http://psyco.sourceforge.net/)
        the Sieve of Atkin is faster as we expect it to be.
        Let's use this simpler version. """
    if end < 2: return []
    lng = ((end / 2) - 1 + end % 2)
    sieve = [True]*(lng+1)
    for i in range(int(math.sqrt(end)) >> 1):
        if not sieve[i]: continue
        for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):
            sieve[j] = False
    primes = [2]
    primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])
    return primes

is_prime = {}
def compute_factors(limit):
  primes   = sieveOfErat(limit)
  for p in primes:
    is_prime[p] = True

  factors = [[],[]] # 1 has no prime factors. (1 is a unit)

  for i in xrange (2, limit + 1):
    if is_prime.has_key(i):
      factors.append([i])
    else:
      n = i
      for p in primes: # at leat a prime must divide i now
        if n % p == 0:
          factors.append([p] + factors[n / p])
          break
  return factors

def wanted_factors(A, B, P):
  f = compute_factors(B + 1)
  res = {}
  for i in xrange(A, B+1):
    x = set()
    for fa in f[i]:
      if fa >= P:
        x.add(fa)
    res[i] = x
  return res

def unique_sets(factors, A, B):
  for i in xrange(A, B + 1):
    factors[i].add(i + 100000000)
  sigue = 1
  while sigue:
    sigue = 0
    for i in xrange(A, B + 1):
      for j in xrange(i + 1, B + 1):
        set1 = factors[i]
        set2 = factors[j]
        if len(set1.intersection(set2)) > 0:
          factors[i] = factors[i].union(factors[j])
          factors[j] = set()
          sigue = 1
      if sigue == 1:
        break

  s = 0
  for i in xrange(A, B + 1):
    if len(factors[i]):
      s+= 1
  return s

def solve(A, B, P):
  f =  wanted_factors (A, B, P)
  print unique_sets(f, A, B)

###

if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  NTEST =  int(f.readline())
  for i in xrange(NTEST):
    print ('Case #%d:' % (i + 1)),
    A, B, P = map(int, f.readline().strip().split())
    solve(A, B, P)
