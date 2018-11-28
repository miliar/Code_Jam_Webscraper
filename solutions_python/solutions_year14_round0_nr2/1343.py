#!/usr/bin/python

import sys
import math

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)
  toks = sys.stdin.readline().strip().split()
  C = float(toks[0])
  F = float(toks[1])
  X = float(toks[2])
  # print
  # print C,F,X

  if X <= C:
    T = X/2
    # print T
  else:
    n = math.ceil(X/C - 1 - 2/F) # num of farms needed
    if n >= 0:
      Rf = 2 + F*n  # final rate
      Tf = X/Rf     # final time slice

      Tn = 0        # time to buy n farms
      for i in range(int(n)):
        Tn += 1 / (2 + i*F)
      Tn *= C

      # print n,Rf,Tf,Tn
      T = Tn + Tf
      # print T
    else:
      T = X/2
      # print T

  # CF = C/F

  # R = 2
  # T = 0
  # # print T, R
  # while True:
  #   if X <= C:
  #     T += X/R
  #     # print T, R, "quick"
  #     break
  #   else:
  #     T += C/R
  #   # have C cookies now

  #   p = R*CF + C
  #   if p >= X:
  #     T += (X-C)/R
  #     # print T, R, "don't buy"
  #     break
  #   else:
  #     # T += CF
  #     R += F
  #     # print T, R, "buy"

  print "Case #%d: %.7f" % (test+1, T)

