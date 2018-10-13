#! /usr/bin/env python

import os
import sys
import math
import copy
import string
import numpy as np


def solve(c):
  if len(c) == 0:
    return 0;

  xor = c[0];
  for x in c[1:]:
    xor ^= x;
  if xor != 0:
    return 0;

  # it is possible 
  return sum(c) - min(c)

if __name__=='__main__':
  f = open(sys.argv[1], 'r');
  T = int(f.readline());
  
  case = 0;
  while case < T:
    case += 1;
    nc = int(f.readline());
    l = f.readline().split();

    n = solve(map(int, l));

    if n > 0:
      print 'Case #%d: %d' % (case, n)

    else:
      print 'Case #%d: NO' % case;

