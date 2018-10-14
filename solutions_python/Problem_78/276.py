#!/usr/bin/python

import sys
f = open(sys.argv[1], 'r')
cases = int(f.readline())
case = 0

for l in f.readlines():
  case += 1
  #do something
  line = l.split()
  N = int(line[0]) + 1
  Pd = int(line[1])
  Pg = int(line[2])
  
  output = "Broken"

  for d in range(1, N):
    wind = (Pd*d)/100
    lostd = d - int(wind)
    if wind%1 != 0:
      continue
    larger  = int(wind+1)
    larger *= 100
    larger += 1
    for g in range(d, larger):
      wing = (Pg*g)/100
      lostg = g-int(wing)
      if wing%1 != 0:
        continue
      if wing >= wind:
        if lostg >= lostd:
          output = "Possible"
        
  print("Case #{0}: {1}".format(case,output))

