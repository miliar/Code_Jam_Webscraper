#!/usr/bin/env python

import sys


def solve(path):
  with open(path) as fin:
    numTests = int(fin.next().strip())
    for test in xrange(numTests):
      a1 = int(fin.next().strip())
      for _ in xrange(a1 - 1):
        fin.next()
      possibleCards1 = set([int(num) for num in fin.next().strip().split()])
      for _ in xrange(4 - a1):
        fin.next()
      a2 = int(fin.next().strip())
      for _ in xrange(a2 - 1):
        fin.next()
      possibleCards2 = set([int(num) for num in fin.next().strip().split()])
      result = possibleCards1 & possibleCards2
      if len(result) == 1:
        output = result.pop()
      elif len(result) == 0:
        output = "Volunteer cheated!"
      else:
        output = "Bad magician!"
      print "Case #%i: %s" % (test + 1, output)
      # Clean up
      for _ in xrange(4 - a2):
        fin.next()


if __name__ == "__main__":
  solve(sys.argv[1])
