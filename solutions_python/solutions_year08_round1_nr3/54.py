#!/usr/bin/env python

import sys, math

lsqrt_five = list('223606797749978969640917366873127623544061835961152572427089')

if __name__ == '__main__':
  T = int(sys.stdin.readline().strip())

  for i in xrange(T):
    ones = 1
    sqrts = 0
    n = int(sys.stdin.readline().strip())
    for j in xrange(n):
      nones = 5 * sqrts + 3 * ones
      nsqrts = 3 * sqrts + ones
      sqrts = nsqrts
      ones = nones
      #print ones, sqrts
    #ones %= 1000000000
    #sqrts %= 1000000000
    length = len(list(str(sqrts)))
    sqrt_five = 0
    for j in xrange(length + 1):
      sqrt_five = sqrt_five * 10 + int(lsqrt_five[j])
    #print sqrts, sqrt_five,
    sqrts = sqrts * sqrt_five
    for j in xrange(length):
      sqrts = int(sqrts / 10)
    tot = ones + sqrts
    #print tot, ones, sqrts,
    tot = int(tot % 1000)
    #print tot
    if tot < 1:
      print 'Case #%d: 000' % i + 1
    elif tot < 10:
      print 'Case #%d: 00%d' % (i + 1, tot)
    elif tot < 100:
      print 'Case #%d: 0%d' % (i + 1, tot)
    else:
      print 'Case #%d: %d' % (i + 1, tot)
