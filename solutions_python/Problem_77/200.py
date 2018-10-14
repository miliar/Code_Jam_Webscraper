#!/usr/bin/env python
#python 2.6 and above (Fraction)

import fractions
import functools
INF = 2**1000

# Strategy S
# If we hold all but 2 and hit, 1/4 chance that nothing will be sorted.
# If we hold only sorted, and hit remaining r, only 1/r! chance that we have
#   not brought the problem down?

def Memoize(f):
  """ A decorator to memoize multiple variable pure functions."""
  lookup_table = {}
  @functools.wraps(f)
  def Wrapper(*args):
    n = tuple(args)
    if not lookup_table.has_key(n):
      lookup_table[n] = f(*args)
    return lookup_table[n]
  return Wrapper

@Memoize
def Derangement(n):
  if n == 0:
    return 1
  if n == 1:
    return 0
  if n == 2:
    return 1
  return (n-1) * (Derangement(n-1) + Derangement(n-2))

@Memoize
def nCk(n, k):
  assert (k <= n)
  if k == 0 or k == n:
    return 1
  if k == 1 or k == n-1:
    return n
  return nCk(n-1, k-1) + nCk(n-1, k)

@Memoize
def Factorial(n):
  if n == 0:
    return 1
  return n * Factorial(n-1)


@Memoize
def P(n, k):
  """ Return the probability that exactly `k` elements are in their right
  place, after a random shuffle."""
  return fractions.Fraction(nCk(n, k) * Derangement(n-k), Factorial(n))


@Memoize
def AverageHits(n):
  """ Returns the average number of hits required to sort `n` numbers using
  Gorosort, and strategy, S."""
  if n == 0: return 0
  if n == 1: assert False, "We should have never reached here!"
  if n == 2: return fractions.Fraction(2, 1)

  summation = sum([P(n, i) * AverageHits(n-i) for i in range(1, n-1)])

  return (fractions.Fraction(1, 1) + summation)/(fractions.Fraction(1) - P(n, 0))


def CountMisplaced(li):
  count = 0
  for i in range(len(li)):
    if li[i] != i+1:
      count += 1
  return count

def ProcessTestCase(test_case):
  raw_input()
  li = [int(x) for x in raw_input().strip().split()]

  misplaced = CountMisplaced(li)
  # average_hits = AverageHits(misplaced)
  average_hits = misplaced
  print "Case #%d: %.6f"%(test_case+1, average_hits.numerator/float(average_hits.denominator))
  return

def Main():
  test_cases = int(raw_input())
  for t in range(test_cases):
    ProcessTestCase(t)

if __name__ == '__main__':
  Main()
