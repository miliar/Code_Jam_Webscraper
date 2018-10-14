import operator
import itertools
import sys
import numpy
from sys import stdin

#def binomialCoeff(n, k):
#  result = 1
#  for i in range(1, k+1):
#    result = result * (n-i+1) / i
#
#  return result
#
#def derangement(n, k):
#  if n == k:
#    return 1.0
#  else:
#    return binomialCoeff(n, k) * round(math.factorial(n-k)/math.e)
#
#  
#def derangements(n):
#  nfact = math.factorial(n)
#  #nfact = 1.0
#  return [derangement(n, k)/nfact for k in xrange(0, n-1)]
#
#def derangeTable(n):
#  res = []
#  for i in xrange(2, n+1):
#    row =([0.0]*(n-i))
#    row.extend(derangements(i))
#    res.append(row)
#
#  res.reverse()
#  return res

def solve(nums):
  c = 0
  for i in xrange(0, len(nums)):
    if i != nums[i] - 1:
      c += 1

#  if c % 2 == 1:
#    c -= 1

  return c * 1.0

f = stdin
#f = open('p1-4inp.txt')
cases = int(f.readline())
for i in xrange(0, cases):
  f.readline()
  nums = map(int, f.readline().split())
  res = solve(nums)
  print 'Case #%d: %6f' % (i+1, res)

