#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from math import sqrt
from sys import stdin

def main():
  def is_palyndrome(num):
    s = str(num)
    return s == s[::-1]

  def check(num):
    v = int(sqrt(num))
    return v * v == num and is_palyndrome(num) and is_palyndrome(v)

  t = int(stdin.readline())
  for ti in xrange(1, t + 1):
    a, b = [int(s) for s in stdin.readline().strip().split()]
    print 'Case #%i: %s' % (ti, len(filter(check, xrange(a, b + 1))))

if __name__ == '__main__':
  main()