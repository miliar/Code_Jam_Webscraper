#!/usr/bin/python
import sys

f = open(sys.argv[1],'r')
n = int(f.readline())
for tc in range(1,n+1):
  line=f.readline().rstrip('\n').split(" ")
  N=int(line[0])
  M=int(line[1])
  fs=dict()
  fs[""]=dict()
  Result=0
  for e in range(N):
    ndir=f.readline().rstrip('\n').split('/')
    act=fs
    for i in range(len(ndir)):
      if not ndir[i] in act:
        act[ndir[i]]=dict()
      act=act[ndir[i]]
  for ee in range(M):
    ndir=f.readline().rstrip('\n').split('/')
    act=fs
    for i in range(len(ndir)):
      if not ndir[i] in act:
        act[ndir[i]]=dict()
#        print '"%s"'%ndir[i]
        Result=Result+1
      act=act[ndir[i]]
  print "Case #%d: %s"%(tc,Result)
