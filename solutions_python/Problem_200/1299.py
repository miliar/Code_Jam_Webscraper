#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def get_last(digits):
  if len(digits) == 1:
    return digits[0]
  if int(digits[0]) > int(digits[1]):
    return '%s%s'%(str(int(digits[0])-1).lstrip('0'), '9'*(len(digits)-1))
  elif int(digits[0]) < int(digits[1]):
    return digits[0] + get_last(digits[1:])
  else:
    k = 1
    while k < len(digits) and digits[0] == digits[k]:
      k += 1
    if k == len(digits):
      return digits
    elif int(digits[0]) < int(digits[k]):
      return digits[0]*k + get_last(digits[k:])
    else:
      return '%s%s'%(str(int(digits[0])-1).lstrip('0'), '9'*(len(digits)-1))

def solve(t, i):
  N = t[i]
  print 'Case #%d: %s'%(i+1, get_last(N))

if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    buf = f.read()
  t = buf.split("\n")
  nb_tests = int(t[0])
  t = t[1:]
  for k in xrange(0, nb_tests):
    solve(t, k)
