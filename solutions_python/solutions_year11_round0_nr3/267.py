import operator
import itertools
import sys
from sys import stdin

def solve(candies):
  candies.sort()
  if reduce(operator.xor, candies) != 0:
    return 'NO'
  else:
    return str(sum(candies) - min(candies))

f = stdin
#f = open('p1-3inp.txt')
cases = int(f.readline())
for i in xrange(0, cases):
  f.readline()
  candies = map(int, f.readline().split())
  res = solve(candies)
  print 'Case #%d: %s' % (i+1, res)
