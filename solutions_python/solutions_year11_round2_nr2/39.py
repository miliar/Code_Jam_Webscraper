#!/usr/bin/python
import sys
import string
import math

# Open in- and output files
f = "" if len(sys.argv) < 2 else sys.argv[1]
i = open(f, 'r')
o = open("%s.out" % f, 'w')

# Parse input file
cases = int(i.readline())

def time(elem):
  return abs(elem[1] - elem[0])

for case in range(1, cases + 1):  
  # chunks = i.readline().strip().split(" ")
  # OR
  # value = int(i.readline()
  stands = []

  (C, D) = i.readline().strip().split(" ")

  C = int(C)
  D = int(D)    

  psum = 0

  for n in range(0, C):
    (P, V) = i.readline().strip().split(" ")
    psum += int(P) * int(V)
    for v in range(0,int(V)):
      stands.append([int(P), int(P)])

  stands.sort()
  w = stands[0][0] + D

  for stand in stands[1:]:
    stand[1] = max(w, stand[0])
    w = stand[1] + D
      
  times = []
  for stand in stands:
    times.append(stand[1] - stand[0])

  #print stands
  #print times
  need = (float(abs(min(times)) + abs(max(times))) / 2)
    

  result = "Case #%i: %s" % (case, need)
  print result
  o.write("%s\n" % result)

# Close in- and output
i.close()
o.close()
