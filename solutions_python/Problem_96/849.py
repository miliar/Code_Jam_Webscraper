#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
#
# gcj_qualify_B.py
#
# mariopal
# 4-2012
#
# Using Python 2.7.3rc2 in Linux (Debian Sid):
# $ ./gcj_qualify_B.py input.txt > output.txt
#
"""
Use: python gcj_qualify_B.py input.txt > output.txt
"""
# ----------------------------------------------------------------------------
import sys

def out(x):
  sys.stdout.write(str(x))
def out_ln(x):
  sys.stdout.write(str(x) + "\n")
# ----------------------------------------------------------------------------


def test(N, S, p, tp):
  R = 0
  Nn = p + (p-1) + (p-1)
  if Nn < 0:  Nn = p*3
  Ns = p + (p-2) + (p-2)
  if Ns < 0:  Ns = p*3
  ns = 0

  for tsi in tp:
    ti = int(tsi)

    if ti >= Nn:  R += 1
    else:
      if ns < S:
        if ti >= Ns:
          R += 1
          ns += 1

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
    line = ftest.readline()
    p = line[:-1].split(" ")
    R = test(int(p[0]),int(p[1]),int(p[2]),p[3:])
    out_ln("Case #" + str(t) + ": " + str(R))
    t += 1
  ftest.close()
#main


if __name__ == '__main__':
  main()
