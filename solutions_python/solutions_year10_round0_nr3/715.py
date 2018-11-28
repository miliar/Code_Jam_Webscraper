#!/usr/bin/python


T=int(raw_input())
for case in xrange(T):
  [R,k,N]=map(int,raw_input().rstrip().split())
  g=map(int,raw_input().rstrip().split())
  index=0
  total=0
  for r in xrange(R):
    in_so_far=0
    count=0
    while (in_so_far+g[index])<=k and count<N:
     in_so_far+=g[index]
     index=(index+1)%len(g)
     count+=1
    total+=in_so_far
  print 'Case #%d: %d'%(case+1,total)
