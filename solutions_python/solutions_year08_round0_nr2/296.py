#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
#
# gcj_qualify_B.py
#
# mariopal
# 6-2008
#
# Using Python 2.5.2 in Linux (Debian Sid):
# $ ./gcj_qualify_B.py input.in > output.out
#
"""
Use: python gcj_qualify_B.py input.in > output.out
"""
# ----------------------------------------------------------------------------
import sys

def out(x):
  sys.stdout.write(str(x))
def out_ln(x):
  sys.stdout.write(str(x) + "\n")
# ----------------------------------------------------------------------------


def test(T, L):
  L.sort(lambda x,y: cmp(x[0], y[0]))

  nA = 0
  nB = 0
  A = []
  B = []

  for e in L:
    if e[2]==0: #------------------------ A ------------------------
      if len(A) == 0:
        a = -2
      else:
        for a in A:
          if a <= e[0]:
            A.remove(a)
            B.append(e[1] + T)
            a = -1
            break
      if a != -1:
        nA += 1
        B.append(e[1] + T)

    else:       #------------------------ B ------------------------
      if len(B) == 0:
        b = -2
      else:
        for b in B:
          if b <= e[0]:
            B.remove(b)
            A.append(e[1] + T)
            b = -1
            break
      if b != -1:
        nB += 1
        A.append(e[1] + T)

  return (nA, nB)
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
    L = []
    line = ftest.readline()
    T = int(line)
    line = ftest.readline()
    param = line[:-1].split(" ")
    a = int(param[0])
    b = int(param[1])

    while a:
      line = ftest.readline()
      param = line[:-1].split(" ")
      p = param[0].split(":")
      i = int(p[0])*60 + int(p[1])
      p = param[1].split(":")
      f = int(p[0])*60 + int(p[1])
      L.append((i, f, 0))
      a -= 1

    while b:
      line = ftest.readline()
      param = line[:-1].split(" ")
      p = param[0].split(":")
      i = int(p[0])*60 + int(p[1])
      p = param[1].split(":")
      f = int(p[0])*60 + int(p[1])
      L.append((i, f, 1))
      b -= 1

    param = line[:-1].split(" ")
    nA, nB = test(T, L)
    out_ln("Case #" + str(t) + ": " + str(nA) + " " + str(nB))
    t += 1
  ftest.close()
#main


if __name__ == '__main__':
  main()
