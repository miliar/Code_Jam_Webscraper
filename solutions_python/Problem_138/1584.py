#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in xrange(t):
  n = int(f.readline())
  naomi = [float(x) for x in f.readline().split()]
  ken = [float(x) for x in f.readline().split()]
  naomi.sort()
  ken.sort()
  i = 0
  deceit = 0
  while(naomi[i]<ken[0]):
    i += 1
    if (i >= n):
      break
  j = 0
  while( i <n and j <n):
    if(ken[j] < naomi[i]):
      deceit += 1
      i += 1
      j += 1
    else:
      i += 1
  j = n-1
  i = n-1
  war = 0
  while (i >= 0 and j >= 0):
    if(ken[j] > naomi[i]):
      war += 1
      i -= 1
      j -= 1
    else:
      i -= 1
  print "Case #" + str(case+1) + ":", deceit, n-war
