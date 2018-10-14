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
def process(U, probs):

#  print U, probs

  new_factor = [1]
  new_probs  = [probs[0]]
  for p in probs[1:]:
    if p in new_probs:
      k = new_probs.index(p)
      new_factor[k] += 1
    else:
      new_probs.append(p)
      new_factor.append(1)

  probs = [[new_probs[k], new_factor[k]] for k in xrange(len(new_probs))]

#  print probs, U
  while U > 0:
    if len(probs) == 1:
      probs[0][0] = min([1, probs[0][0]+U/probs[0][1]])
      U = 0
    else:
      probs.sort()
      required_p = (probs[1][0]-probs[0][0]) * probs[0][1]
      if U >= required_p:
        U -= required_p
        probs[1][1] += probs[0][1]
        del probs[0]
      else:
        probs[0][0] += U/probs[0][1]
        U = 0

#    print probs, U

  porbability = 1.0
  for p in probs:
    porbability *= p[0]**p[1]

  return '%.9f'%(porbability)


#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  data  = [x for x in lines[0].split()]
  N     = int(data[0]) 
  K     = int(data[1]) 
  lines = lines[1:]

  U     = float(lines[0])
  lines = lines[1:]

  probs = [float(x) for x in lines[0].split()]
  lines = lines[1:]

  solution = process(U, probs)

  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
