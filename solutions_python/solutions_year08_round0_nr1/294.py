#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
#
# gcj_qualify_A.py
#
# mariopal
# 7-2008
#
# Using Python 2.5.2 in Linux (Debian Sid):
# $ ./gcj_qualify_A.py input.in > output.out
#
"""
Use: python gcj_qualify_A.py input.in > output.out
"""
# ----------------------------------------------------------------------------
import sys

def out(x):
  sys.stdout.write(str(x))
def out_ln(x):
  sys.stdout.write(str(x) + "\n")
# ----------------------------------------------------------------------------


def test(S, Q):
  R = 0

  while len(Q):
    sn = 0
    sswap = False
    for s in S:
      n = 0
      swap = False
      for q in Q:
        if q == s:
          swap = True
          break
        n += 1
      if n > sn:
        if swap: sswap = True
        sn = n

    if sn == len(Q):
      Q = []
    elif sswap:
      Q = Q[sn:]
      R += 1

  return R
#test


def main():
  if len(sys.argv) > 1:
    inputfile = sys.argv[1]
  else:
    print __doc__
    return

  ftest = open(inputfile, "rb")
  line = ftest.readline()
  numtests = int(line)
  t = 1
  while t <= numtests:
    S = []
    Q = []
    line = ftest.readline()
    nS = int(line)
    while nS:
      line = ftest.readline()
      S.append(line[:-1])
      nS -= 1
    line = ftest.readline()
    nQ = int(line)
    while nQ:
      line = ftest.readline()
      Q.append(line[:-1])
      nQ -= 1
    R = test(S, Q)
    out_ln("Case #" + str(t) + ": " + str(R))
    t += 1
  ftest.close()
#main


if __name__ == '__main__':
  main()
