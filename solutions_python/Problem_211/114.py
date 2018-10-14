#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, shutil, subprocess
import signal
import re
import math, random
import numpy as np

sys.setrecursionlimit(2000000000)
signal.signal(signal.SIGINT, signal.SIG_DFL)



def test(verbose):
  K, N = map(int, input().split())
  U = float(input())
  P = list(map(float, input().split()))
  
  if not verbose:
    return
  
  P.sort()
  P.append(1.0)
  
  while P[0] != 1.0 and U != 0.0:
    a = P[0]
    n = 1
    while n < len(P) and P[n] == P[n-1]:
      n += 1
    b = P[n]
    v = min(b - a, U / n)
    for i in range(n):
      P[i] += v
    U -= v * n
  
  ans = 1.0
  for p in P: ans *= p
  
  print('%.6f' % ans)


if __name__ == '__main__':
  z = int(sys.argv[1]) if len(sys.argv) > 1 else -1

  t = int(input())
  for i in range(1, t+1):
    verbose = z in (-1, i)
    if verbose:
      print('Case #%d: ' % i, end='')
    test(verbose)

