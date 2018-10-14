#!/usr/bin/env python
# -*- coding: latin1 -*-

from string import strip, split 

import sys


def print_output(cases, list_sol):
  for i in range(0,cases):
    print "Case #%d: %s" % ( i+1, list_sol[i] )


name_infile = sys.argv[1]

f = open(name_infile, 'r')

#first line
line = f.readline()
line = line.strip()

cases = int(line)

l_sol = []

for line in range(0,cases):
  line = f.readline()
  line = line.strip()
  line = line.split()
  N= int(line[0])
  k= int(line[1])

  aux = (2**N)-1
  
  if (k & aux) == aux:
    l_sol.append('ON')
  else:
    l_sol.append('OFF')


print_output(cases, l_sol) 
f.close()

