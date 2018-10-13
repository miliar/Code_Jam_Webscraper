#!/usr/bin/env python
# -*- coding: iso8859-1 -*-
#
# gcj_qualify_A.py
#
# mariopal
# 4-2012
#
# Using Python 2.7.3rc2 in Linux (Debian Sid):
# $ ./gcj_qualify_A.py input.txt > output.txt
#
"""
Use: python gcj_qualify_A.py input.txt > output.txt
"""
# ----------------------------------------------------------------------------
import sys

def out(x):
  sys.stdout.write(str(x))
def out_ln(x):
  sys.stdout.write(str(x) + "\n")
# ----------------------------------------------------------------------------


Ginp = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

Gout = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"


rosetta = {}
for i in range(ord('a'),ord('z')+1):
  rosetta[chr(i)] = '#'

total = len(Ginp)
n = 0
while n < total:
  rosetta[Ginp[n]] = Gout[n]
  n += 1

rosetta['z'] = 'q'
rosetta['q'] = 'z'
rosetta['\n'] = ''


def test(line):
  R = ""
  for i in line:
    R += rosetta[i]

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
    R = test(line)
    out_ln("Case #" + str(t) + ": " + R)
    t += 1
  ftest.close()
#main


if __name__ == '__main__':
  main()
