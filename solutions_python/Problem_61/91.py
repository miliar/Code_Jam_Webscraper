#!/usr/bin/python
from sys import stdin

res = [0, 0, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 40265, 68060, 13335, 84884]

  
TTT = int(stdin.readline())
for ttt in range(1,TTT+1):
  n = int(stdin.readline())
  print "Case #%d: %d" % (ttt,res[n])
