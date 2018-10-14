#!/usr/bin/python
#
# Many Prizes - Google Code Jam 2013 Round 2 Problem B

import sys
inp=sys.stdin
cases=int(inp.readline())
for case in xrange(cases):
  data=inp.readline().strip().split()
  n=int(data[0])
  p=int(data[1])
  if p==1:
    guarantee=0
    could=0
  elif p==2**n:
    guarantee=2**n-1
    could=2**n-1
  elif p>2**(n-1):
    could=2**n-2
    #find the earliest round in which a team must win in order to
    #get a prize
    x=2**(n-1)
    teams=x
    rounds=1
    while p>teams:
      x/=2
      teams+=x
      rounds+=1
    guarantee=2**rounds-2
  else:
    guarantee=0
    #find the number of required wins at the start of the tournament
    #this one is off-by-one. 
    teams=2**(n-1)
    rounds=1
    while p<teams:
      teams/=2
      rounds+=1
    could=2**n-2**rounds
  print "Case #"+repr(case+1)+":",guarantee,could
