#!/usr/bin/python

from sys import argv

if len(argv) > 1:
  filename = argv[1]
else:
  filename = "test.in"

f = open(filename)

numCases = int(f.readline())

for case in range(1, numCases + 1):
  output = ""
  num = int(f.readline().strip())
  x1 = map(lambda x:int(x), f.readline().split())
  x2 = map(lambda x:int(x), f.readline().split())

  x1.sort()
  x2.sort()
  x2.reverse()
  
  tot = 0
  for x in range(0, num):
    tot += x1[x]*x2[x]
    
  print "Case #"+str(case)+": " + str(tot)
