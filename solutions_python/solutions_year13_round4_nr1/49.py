#!/usr/bin/python
#
# Ticket Swapping - Google Code Jam 2013 Round 2 Problem A

import sys
inp=sys.stdin
cases=int(inp.readline())
for case in xrange(cases):
  data=inp.readline().strip().split()
  stops=int(data[0])
  trips=int(data[1])
  entrances=[]
  exits=[]
  properdisc=0
  for i in range(trips):
    data=inp.readline().strip().split()
    ent=int(data[0])
    ex=int(data[1])
    passengers=int(data[2])
    #calculate proper discount
    distance=ex-ent
    properdisc+=passengers*distance*(distance-1)/2
    #store trip data
    entrances.append([ent,passengers])
    exits.append([ex,passengers])
  #process passengers in order of exit
  entrances.sort()
  exits.sort()
  actualdisc=0
  entpointer=0
  while len(exits)>0:
    exitstation=exits[0][0]
    while entpointer<len(entrances)-1 and entrances[entpointer+1][0]<=exitstation:
      entpointer+=1
    enterstation=entrances[entpointer][0]
    passengers=min(entrances[entpointer][1],exits[0][1])
    distance=exitstation-enterstation
    actualdisc+=passengers*distance*(distance-1)/2
    if passengers==exits[0][1]:
      del exits[0]
    else:
      exits[0][1]-=passengers
    if passengers==entrances[entpointer][1]:
      del entrances[entpointer]
      if entpointer>0:
        entpointer-=1
    else:
      entrances[entpointer][1]-=passengers
  print "Case #"+repr(case+1)+": "+repr(int(actualdisc-properdisc))
