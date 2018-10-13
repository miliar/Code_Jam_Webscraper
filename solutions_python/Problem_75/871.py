#!/usr/bin/env python

"""
Contest: Google Code Jam Qualification Round
Problem: Magicka
"""

import sys

input_file = open(sys.argv[1])
numcases = int(input_file.readline().strip())
for i in xrange(1, numcases+1):
  fields = input_file.readline().split()

  explode = dict()
  dlist = dict()  
  relations = dict()
  for b1 in ('Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'):
    for b2 in ('Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'):
      relations[(b1, b2)] = 0
    dlist[b1] = []
      
  C = int(fields[0])
  for combo in fields[1:C+1]:
    relations[(combo[0], combo[1])] = combo[2]
    relations[(combo[1], combo[0])] = combo[2]

  
  D = int(fields[C+1])
  for oppo in fields[C+2:C+2+D]:
    dlist[oppo[0]].append(oppo[1])
    dlist[oppo[1]].append(oppo[0])
  
  N = int(fields[C+2+D])
  invoke = fields[-1]
  
  result = []
  bases = []
  prev = 2

  for x in invoke:
    if prev == 2:
      if explode.get(x) == True:
        explode = dict()
        prev = 2
        result = []
        bases = []
      else:
        for m in dlist[x]:
          explode[m] = True
        prev = x
        result.append(prev)
        bases.append(prev)
      continue
    if relations[(prev, x)] == 0:
      if explode.get(x) == True:
        explode = dict()
        prev = 2
        result = []
        bases = []
      else:
        for n in dlist[x]:
          explode[n] = True
        prev = x
        result.append(prev)
        bases.append(prev)
    else:
      result.pop()
      bases.pop()
      explode = dict()
      for k in bases:
        for d in dlist[k]:
          explode[d] = True
      result.append(relations[(prev, x)])
      prev = 2
  
  sys.stdout.write("Case #" + str(i) + ": [")
  if result != []:
    for p in result[:-1]:
      sys.stdout.write(p + ", ")
    sys.stdout.write(result[-1] + "]\n")
  else:
    sys.stdout.write("]\n")
  