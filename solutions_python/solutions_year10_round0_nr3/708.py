#!/usr/bin/env python
# -*- coding: latin1 -*-

from collections import deque
from string import strip, split 

import sys


def euros_made(rounds, max_people, n_groups, groups):
   
   if n_groups == 1: return groups[0] * rounds

   queue = deque(groups)
   euros = 0

   for i in range(0,rounds):
      people_on = 0
      groups_on = 0
      while people_on < max_people and groups_on < n_groups:
        size_group = queue[0]#queue.popleft()
        if ( people_on + size_group ) <= max_people: 
           groups_on += 1
           people_on += size_group
           euros += size_group
           queue.append( queue.popleft() )
        else: break
   return euros 


def print_output(cases, list_sol):
  for i in range(0,cases):
    print "Case #%d: %d" % ( i+1, list_sol[i] )


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
  r_rounds = int(line[0])
  k_people= int(line[1])
  n_groups = int(line[2])

  line = f.readline()
  line = line.strip()
  l_groups = [int(x) for x in line.split()]

  l_sol.append( euros_made(r_rounds, k_people, n_groups, l_groups) )
  

print_output(cases, l_sol) 
f.close()

