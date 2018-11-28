#!/usr/bin/env python
import numpy

def indivCase(CaseNo, Smax, levels):
  # only need max of 1000, working off of large dataset
  # make levels a string
  # basically need enough running count to reach Smax
  # add int(levels[i]) to count, decrement running count, increment index
  ## if running count runs out, add 1 to more then increment index
  ## OR increment index by num of running count, 
  ## if 0, add 1 more, increment by 1
  more = 0;
  run = 0;
  for i in range(0,Smax):
    run += int(levels[i])
    run -= 1
    if run < 0:
      run = 0
      more += 1
  caseout =  'Case #' + str(CaseNo)+ ': '+ str(more)
  print caseout

###
f = open("A-large.in", 'r')
cases = int(f.readline())
case = 0
for line in f.readlines():
  arr = line.split()
  case += 1
  indivCase(case, int(arr[0]), str(arr[1]))

