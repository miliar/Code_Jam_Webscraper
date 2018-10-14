#!/usr/bin/python

import sys
import string
import logging
import time

import re

def digits(n):
  acc = []

  while n > 0:
    acc.insert(0, n % 10)
    n = n / 10

  return acc

def fix(tail):
  s = sorted(tail)
  if tail == list(reversed(s)):
    return None

  first = tail[0]
  biggerthanfirst = filter(lambda x: x > first, s)
  if not biggerthanfirst:
    return None
  b = biggerthanfirst[0]
  s.remove(b)
  next = [b] + s
  assert next != tail
  return next

def next(prevint):
  prevdigits = digits(prevint)
  if prevdigits == list(reversed(sorted(prevdigits))):
    # As good as we're going to get in this mode, so 
    # insert a 0.
    out = sorted(prevdigits)
    # Count the zeroes and then remove them:
    zeroes = out.count(0)
    for i in range(zeroes):
      out.remove(0)
    out = out[0:1] + [0]*(zeroes+1) + out[1:]
    
  else:
    # Fix the tail
    out = None
    for i in range(2, 1+len(prevdigits)):
      x = fix(prevdigits[-i:])
      if x:
        out = prevdigits
        out[-i:] = x
        break
    if out is None:
      __import__("pdb").set_trace() 

  return undigits(out)


def undigits(x):
  acc = 0
  mult = 1
  for i in reversed(x):
    acc += i*mult
    mult *= 10
  return acc

if __name__ == "__main__":

  if True:
    assert digits(123) == [1,2,3]
    assert undigits([1,2,3]) == 123
    assert next(321) == 1023
    assert next(123) == 132
    assert next(115) == 151
    assert next(1051) == 1105
    assert next(6233) == 6323
    assert next(7654) == 40567
    assert next(9929888877777666665555544444333332222211111) != 0
    assert next(590) == 905
    assert next(980) == 8009

  logging.basicConfig(level=logging.INFO)
  input = file(sys.argv[1])
  num_problems = int(input.readline().strip())
  for i in range(num_problems):
    prev = input.readline().strip()
    prevint = int(prev)
    logging.info(prev)
    n = next(prevint)
    assert n > prevint, prevint
    print "Case #%d: %d" % (i+1, next(prevint))
