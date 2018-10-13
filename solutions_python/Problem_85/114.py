#!/usr/bin/python

import sys

fp = open(sys.argv[1],"r")
T = int(fp.readline())

for c in range(T): # for all cases
  v1 =  map(int,(fp.readline().split()))
  L = v1[0]
  t = v1[1]
  N = v1[2]
  C = v1[3]
  a = v1[4:]
  # build list of distances
  starlist = (int(N/C)+1)*a # repeated
  starlist = starlist[0:N] # only N stars
#  print starlist
  s1 = 0
  i = 0
  while s1<(t/2) and i<N:
    s1+=starlist[i]
    i+=1
  rest = s1-t/2
  speedup = [rest]+starlist[i:N]
  speedup.sort()
  speedup.reverse()
  # if boost is to be made on first available star
#  print speedup
#  print rest
#  print s1
  if rest >= speedup[L-1]:
    tot = 2*s1-2*rest+sum(speedup[0:L])+2*sum(speedup[L:])
  else:
    tot = 2*s1+sum(speedup[0:L])+2*sum(speedup[L:])-2*rest
  print "Case #"+str(c+1)+": "+str(tot)

