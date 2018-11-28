#!/usr/bin/env python

import os, numpy, math, sys, string

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])
output = ''

curLine = 1
for t in range(0,T):
  M=int(lines[curLine].split()[0])
  #print M
  
  curLine+=1
  
  rows = []
  for z in range(4):
    if (z==M-1):
      for k in range(4):
        rows.append(lines[curLine].split()[k])
      #print rows
    curLine+=1
  
  N=int(lines[curLine].split()[0])
  #print N
  curLine+=1
  cols = []
  for z in range(4):
    if (z==N-1):
      for k in range(4):
        cols.append(lines[curLine].split()[k])
    curLine+=1
  #print cols
  
  answ = 0
  answVal = -1
  for z in range(4):
    if cols[z] in rows:
      answ+=1
    if (answ==1 and answVal<0):
      answVal = int(cols[z])
  
  output+= "Case #%d: "%(t+1)
  if (answ==1):
    output += "%d\n" % (answVal)
  elif (answ>1):
    output += "Bad magician!\n"
  elif (answ==0):
    output += "Volunteer cheated!\n"
  
  

print output
file(sys.argv[1]+'.res','w').write(output)
