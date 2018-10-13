#!/usr/bin/python

t=input()
for i in xrange(t):
  ss,kk=raw_input().strip().split()
  k=int(kk)
  s=["+-".index(m) for m in ss]
  flips=0
  for j in xrange(len(s)-k+1):
    if s[j]==1:
      flips+=1
      for l in xrange(j,j+k):
        s[l]=1-s[l]
  if max(s[-k:])>0:
    print "Case #"+str(i+1)+": IMPOSSIBLE"
  else:
    print "Case #"+str(i+1)+": "+str(flips)
