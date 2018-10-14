#!/usr/bin/python

def memoize(func):
  def wrapper(*args):
    if args not in memo:
      memo[args] = func(*args)
    return memo[args]
  return wrapper

@memoize
def solve(start):
  left = size
  served = 0
  for el in groups[start:] + groups[:start]:
    if left < el: break
    left -= el
    served += el
    start += 1
  return (served, start % N)

for case in xrange(1, input() + 1):
  (runs, size, N) = map(int, raw_input().split())
  groups = map(int, raw_input().split())
  (euros, cur) = (0, 0)
  memo = {}
  for _ in xrange(runs):
    (served, cur) = solve(cur)
    euros += served

  print "Case #%d: %d" % (case, euros)
