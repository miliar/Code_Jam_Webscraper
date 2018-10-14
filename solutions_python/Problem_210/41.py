#!/usr/bin/env python
import os
import sys
import time

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
def process(PA, PB):

  min_a = 12*60
  min_b = 12*60
  P = []
  for p in PA:
    P.append(p+[0])
    min_a -=  p[1]-p[0]
  for p in PB:
    P.append(p+[1])
    min_b -=  p[1]-p[0]

  P.sort()
#  print P

  ready = False
  while not ready:
    ready = True

    min_dist_a = 100000
    min_k_a    = -1
    min_dist_b = 100000
    min_k_b    = -1
    for k in xrange(len(P)):

      if P[k-1][2] == P[k][2]:  
        if k==0:
          d = 24*60-P[-1][1] + P[0][0]
        else:
          d = P[k][0] - P[k-1][1]
        
        if d == 0:
          continue
  
        if P[k][2] == 0 and min_dist_a > d:
          min_dist_a = d
          min_k_a    = k
        elif P[k][2] == 1 and min_dist_b > d:
          min_dist_b = d
          min_k_b    = k
  
#    print min_a, min_dist_a, min_k_a
#    print min_b, min_dist_b, min_k_b

    if min_dist_a <= min_a:
      min_a -= min_dist_a
      if min_k_a > 0:
        P[min_k_a-1][1] = P[min_k_a][0]
      else:
        P[0][0]   = 0
        P[-1][1]  = 24*60 
      ready = False
    if min_dist_b <= min_b:
      min_b -= min_dist_b
      if min_k_b > 0:
        P[min_k_b-1][1] = P[min_k_b][0]
      else:
        P[0][0]   = 0
        P[-1][1]  = 24*60 
      ready = False

#    print P

    n_changes = 0
    for k in xrange(len(P)):
      if P[k-1][2] != P[k][2]:
        n_changes += 1
      else:
        if k==0:
          d = 24*60-P[-1][1] + P[0][0]
        else:
          d = P[k][0] - P[k-1][1]
        if d != 0:
          n_changes += 2
          
  return '%d'%(n_changes)


#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  data  = [x for x in lines[0].split()]
  NA    = int(data[0])
  NB    = int(data[1])
  lines = lines[1:]
  PA = []
  for k in xrange(NA):
    data  = [int(x) for x in lines[0].split()]
    PA.append(data)
    lines = lines[1:]
  PB = []
  for k in xrange(NB):
    data  = [int(x) for x in lines[0].split()]
    PB.append(data)
    lines = lines[1:]

  solution = process(PA, PB)

  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
