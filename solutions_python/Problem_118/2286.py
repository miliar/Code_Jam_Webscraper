#!/usr/bin/env python
import math

def isFair(n):
  r = list(str(n))
  r.reverse()
  return str(n) == "".join(r)

def isSquare(n):
  return int(math.sqrt(n))**2 == n

if __name__ == '__main__':
  import sys

  f = open(sys.argv[1])
  n_cases = int(f.readline())

  for i in xrange(n_cases):
    start, end = f.readline().split()
    start = math.ceil(math.sqrt(int(start)))
    end = math.floor(math.sqrt(int(end)))
#    print start, end

    results = [x for x in xrange(int(start), int(end+1)) if isFair(x)]
    results = [x for x in results if isFair(x**2)]
#    print " ".join(map(str, results))

    print "Case #%d: %s" % (i+1, len(results))
