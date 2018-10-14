#!/usr/bin/env python
import sys
import math

fp = open(sys.argv[1])

#read parameter
t = int(fp.readline())

#read sets
for i in list(range(t)):
  fs = 0
  (a, b) = [int(x) for x in fp.readline().split()]
  for x in list(range(a, b+1)):
    if math.sqrt(x)%1 == 0:
      number = str(x)
      sqroot = str(int(math.sqrt(x)))
      if number == number[::-1]:
        if sqroot == sqroot[::-1]:
          fs += 1

  print ("Case #", i+1,": ", fs, sep='')

