#!/usr/bin/python
import sys

f = open(sys.argv[1],'r')
n = int(f.readline())
for a in range(1,n+1):
  line=f.readline().split(" ")
  N=int(line[0])
  K=int(line[1])
  T=(2**N)-1
  R="OFF"
  if K & T ==T:
    R="ON"
  print "Case #%d: %s"%(a,R)
