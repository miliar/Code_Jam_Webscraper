#!/usr/bin/env python
import os
import sys
import time
import math

tStart = time.time()

#---------------------------------------------------------------------

ifilename = 'input.in'
ofilename = 'results.out'

args = sys.argv
if len(args) > 1:
  ifilename = args[1]
if len(args) > 2:
  ofilename = args[2]

#---------------------------------------------------------------------
 
ifile = open(ifilename,'r')
data  = ifile.read()
ifile.close()
lines = data.splitlines()
ofile = open(ofilename, 'w')

#---------------------------------------------------------------------
# Functions
def process(K,pancakes):

  sup = []
  for p in pancakes:
    s = math.pi*p[0]**2 + 2*math.pi*p[0]*p[1]
    sup.append(s)

  n = sup.index(max(sup))

  if K == 1:
    return '%.9f'%(sup[n]) 
  else:
    total_sup  = sup[n]
    max_r      = pancakes[n][0]
    p_selected = [pancakes[n]]
    del pancakes[n]
    K -= 1
    while K > 0:
      sup = []
      for p in pancakes:
        if p[0] <= max_r:
          s = 2*math.pi*p[0]*p[1]
          sup.append(s)
        else:
          s = math.pi*p[0]**2 + 2*math.pi*p[0]*p[1] - math.pi*max_r**2
          sup.append(s)
      n = sup.index(max(sup))
      if max_r < pancakes[n][0]:
        max_r = pancakes[n][0]
      p_selected.append(pancakes[n])
      total_sup += sup[n]
      del pancakes[n]
      K -= 1

  return '%.9f'%(total_sup) 


#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  data  = [x for x in lines[0].split()]
  N     = int(data[0])
  K     = int(data[1])
  lines = lines[1:]
  pancakes = []
  for k in xrange(N):
    data  = [int(x) for x in lines[0].split()]
    pancakes.append(data)
    lines = lines[1:]

  solution = process(K,pancakes)

  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
