#!/usr/bin/python

cases=int(raw_input())

def intersect(a,b):
  return (a[0]>b[0] and a[1]<b[1]) or (a[0]<b[0] and a[1]>b[1])

for case in xrange(cases):
  N=int(raw_input())
  count=0
  wires=[]
  for i in xrange(N):
    [l,r]=map(int,raw_input().rstrip().split())
    for wire in wires: 
      if intersect((l,r), wire):
        count+=1
    wires.append((l,r))
   
  print 'Case #%d: %d'%(case+1,count)
