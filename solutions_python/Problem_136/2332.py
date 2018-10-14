#!/usr/bin/env python

import os, numpy, math, sys, string, time

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])
output = ''

curLine = 1

for t in range(0,T):
  C = float(lines[curLine].split(' ')[0])
  F = float(lines[curLine].split(' ')[1])
  X = float(lines[curLine].split(' ')[2])
  #print "C=%.7f ; F=%.7f ; X=%.7f"%(C,F,X)
  
  tt = 0.; #Current time
  c  = 0.; #Current cookies
  cR = 2.; #Current cookie rate
  while (c<X):
    # Time to end with next Farm
    tF  = tt + C/cR + X/(cR+F)
    # Time to End Cookie
    tE = tt + X/cR
    
    if (tF < tE ):
      # Buy a new farm:
      tt += C/cR
      cR += F
    else:
      tt += X/cR
      c = X
      output+= "Case #%d: %.7f\n"%(t+1, tt)
    
  curLine+=1
  

print output
file(sys.argv[1]+'.res','w').write(output)
