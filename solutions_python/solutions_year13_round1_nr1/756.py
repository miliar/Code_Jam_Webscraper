#!/usr/bin/python

import sys, math

def calc3(*ar):
  print(ar)

def dump(msg):
  #print(msg, file=sys.stderr)
  pass

def calc(r, t):
  a1 = 2 * r + 1
  d = 4
  b = 2 * a1 - d
  D = b * b + 8 * t * d
  return math.floor((math.sqrt(D) - b) / (2 * d))


  return cnt

with open(sys.argv[1]) as f:
  for c in range(1,int(f.readline())+1):
    (r, t) = [int(x) for x in f.readline().split()]
    print("Case #%s: %s" % (c, calc(r, t)))

