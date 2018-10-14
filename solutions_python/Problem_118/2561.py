#!/usr/bin/env python

import sys

import math

def is_fair(num):
  if not is_pal(num):
    return False
  
  sqr = is_square(num)
  if sqr is not False:
    if is_pal(sqr):
      return True
  return False

def is_square(num):
    if num == 2: return 2 # Stupid edge cases
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        return int(root)
    return False

def is_pal(num):
  lnum = list(str(num))
  lnlen = len(lnum)
  for ii in xrange(0, int(math.ceil(lnlen / 2.0))):
    if lnum[ii] != lnum[lnlen - 1 - ii]:
      return False
  return True

def solve():
  data = [l.strip() for l in sys.stdin.readlines()]
  tc = int(data.pop(0))
  i = 1
  while i <= tc:

    numFair = 0
    rngF, rngT = map(int, data.pop(0).split(" "))
    for ii in xrange(rngF, rngT):
      if is_fair(ii):
        numFair += 1

    print "Case #%d: %s" % (int(i), numFair)
    i += 1

if __name__ == '__main__':
  solve()
