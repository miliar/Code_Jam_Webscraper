#!/usr/bin/python

t=input()
for i in xrange(t):
  n,c,m=map(int,raw_input().strip().split())
  seats=[0]*(n+1)
  customers=[0]*(c+1)
  for j in xrange(m):
    p,b=map(int,raw_input().strip().split())
    seats[p]+=1
    customers[b]+=1
  rides=max(customers)
  ticketssofar=0
  for j in xrange(1,n+1):
    ticketssofar+=seats[j]
    minrides=int((ticketssofar+j-1)/j)
    if minrides>rides:
      rides=minrides
  maxseat=max(seats)
  promotions=0
  for j in xrange(n+1):
    if seats[j]>rides:
      promotions+=seats[j]-rides
  print "Case #"+str(i+1)+": "+str(rides)+" "+str(promotions)
