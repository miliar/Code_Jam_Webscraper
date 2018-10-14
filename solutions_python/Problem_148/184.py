#!/usr/bin/python

import sys

def findmax(sizes,maxsize):
  #return the index of the largest element less than or equal to
  #maxsize, where sizes is pre-sorted, using binary search,
  #or -1 if no such item
  a=0
  b=len(sizes)-1
  if sizes[a]>maxsize:
    return -1
  if sizes[b]<=maxsize:
    return b
  while a<b-1:
    c=int((a+b)/2)
    if sizes[c]<=maxsize:
      a=c
    else:
      b=c
  return a

#print findmax([10,20,35,36,36,37,40],32)
#print findmax([10,20,35,36,36,37,40],9)
#print findmax([10,20,35,36,36,37,40],41)
#print findmax([10,20,35,36,36,37,40],36)

t=int(sys.stdin.readline())
for caseno in xrange(t):
  lin=sys.stdin.readline().split()
  n=int(lin[0])
  x=int(lin[1])
  lin=sys.stdin.readline().split()
  sizes=[]
  for s in lin:
    sizes.append(int(s))
  sizes.sort()
  ndiscs=0
  while len(sizes)>1:
    maxpair=x-sizes[-1]
    del sizes[-1]
    pairindex=findmax(sizes,maxpair)
    if pairindex>-1:
      del sizes[pairindex]
    ndiscs+=1
  if len(sizes)==1:
    ndiscs+=1
  sys.stdout.write("Case #"+repr(caseno+1)+": "+repr(ndiscs)+"\n")


