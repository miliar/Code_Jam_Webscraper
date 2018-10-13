#!/usr/bin/python

t=input()
for i in xrange(t):
  n,k=map(int,raw_input().strip().split())
  intervals={}
  intervals[n]=1
  while k>0:
    mxgap=max(intervals)
    mxquant=intervals[mxgap]
    mn=int((mxgap-1)/2)
    mx=mxgap-1-mn
    if k<mxquant:
      break
    else:
      k-=mxquant
      del intervals[mxgap]
      if mx in intervals:
        intervals[mx]+=mxquant
      else:
        intervals[mx]=mxquant
      if mn in intervals:
        intervals[mn]+=mxquant
      else:
        intervals[mn]=mxquant        
  print "Case #"+str(i+1)+": "+str(mx)+" "+str(mn)
