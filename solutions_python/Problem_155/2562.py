#!/usr/bin/env python

import os, numpy, math, sys, string

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])
output = ''

curLine = 1
for t in range(0,T):
  Smax=int(lines[curLine].split()[0])
  #print Smax
  
  Si=str(lines[curLine].split()[1])
  
  numbOfAddedPlayers = 0
  curNeededPlayer = 1
  curPlayer = 0
  for i in range(0,len(Si)):
    curPlayer += int(Si[i])
    numbOfAddedPlayers+=(max(curNeededPlayer - curPlayer, 0))
    curPlayer += max(curNeededPlayer - curPlayer, 0)
    curNeededPlayer+=1
  
  output+= "Case #%d: "%(t+1)
  output += "%d\n" % (numbOfAddedPlayers)
  curLine+=1
  

print output
#file(sys.argv[1]+'.res','w').write(output)
