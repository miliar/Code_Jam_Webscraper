#!/usr/bin/python

t=input()
for i in xrange(t):
  n,p=map(int,raw_input().strip().split())
  recipe=map(int,raw_input().strip().split())
  packets=[]
  for j in xrange(n):
    packets.append(map(int,raw_input().strip().split()))
    packets[j].sort()
  servings=[]
  for j in xrange(n):
    servings.append([])
    for p in packets[j]:
      minserv=p*10/(11*recipe[j])
      if p>11*recipe[j]*minserv/10:
        minserv+=1
      maxserv=p*10/(9*recipe[j])
      if p<9*recipe[j]*minserv/10:
        maxserv-=1
      if minserv<=maxserv:
        servings[j].append((minserv,maxserv))
  remain=[len(s) for s in servings]
  kits=0
  while min(remain)>0:
    minserv=servings[0][0][0]
    maxserv=servings[0][0][1]
    for j in xrange(1,n):
      if servings[j][0][0]>minserv:
        minserv=servings[j][0][0]
      if servings[j][0][1]<maxserv:
        maxserv=servings[j][0][1]
    if minserv<=maxserv:
      #make a kit
      kits+=1
      for j in xrange(n):
        del servings[j][0]
        remain[j]-=1
    else:
      #discard unusable packets
      for j in xrange(n):
        if servings[j][0][1]<minserv:
          del servings[j][0]
          remain[j]-=1
  print "Case #"+str(i+1)+": "+str(kits)
