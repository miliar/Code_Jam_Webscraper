#!/usr/bin/python

import sys

T = int(sys.stdin.readline().strip())


for testcase in range(T):
  f = sys.stdin.readline().strip()
  f = f.split(' ')
  N = int(f[0])
  X = int(f[1])
  l = []
  f = sys.stdin.readline().strip()
  s = f.split(' ')
  for x in s:
    l.append(int(x))
  l = sorted(l)
  num = 0
  while len(l) > 0:
      if len(l) == 1:
          num+=1
          break
      if l[0] + l[-1] > X:
          num+=1
          l = l[:-1]
      else:
          num+=1
          l = l[1:-1]
  print ("Case #%d: %s" % (testcase+1, num))

