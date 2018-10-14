#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in xrange(t):
  choice = int(f.readline())
  first_row = None
  second_row = None
  for row in xrange(4):
    if row+1 != choice:
      f.readline()
      continue
    first_row = [int(x) for x in f.readline().split()]
  choice = int(f.readline())
  for row in xrange(4):
    if row+1 != choice:
      f.readline()
      continue
    second_row = [int(x) for x in f.readline().split()]
  first_row.sort()
  second_row.sort()
  i = 0
  j = 0
  intersection = list()
  while ((i<len(first_row)) and (j< len(second_row))):
    if (first_row[i] == second_row[j]):
      intersection.append(first_row[i])
      i += 1
      j += 1
    elif (first_row[i] < second_row[j]):
      i += 1
    else:
      j += 1
  print "Case #" + str(case+1) + ":",
  if (len(intersection) == 1):
    print intersection[0]
  elif (len(intersection) == 0):
    print "Volunteer cheated!"
  else:
    print "Bad magician!"
