#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
  cases += [map(int,fh.readline().strip().split(" "))+[map(int,fh.readline().strip().split(" "))]]
  #print cases[-1]
  if cases[-1][2]!=len(cases[-1][-1]):
    print cases[-1]

try:
  cases += [map(long, fh.readline().strip().split(" "))]
except:
  print "good read"

fh.close()


fh = open("outc.txt","w")
for (i,case) in enumerate(cases):
  R = case[0]
  k = case[1]
  N = case[2]
  G = case[3]
  earned = 0
  for j in range(R):
    on_train = []
    in_line = G
    while len(in_line)>0 and sum(on_train+[in_line[0]])<=k:
      on_train += [in_line[0]]
      in_line = in_line[1:]
    earned += sum(on_train)
    G = in_line+on_train
  print >> fh, "Case #"+str(i+1)+": "+str(earned)

fh.close()
