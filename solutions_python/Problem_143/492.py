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

ncases = int(lines[0])
lines  = lines[1:]
for n in xrange(ncases):
  data = [int(x) for x in lines[0].split()]
  lines  = lines[1:]
  A = data[0]
  B = data[1]
  K = data[2]

  S = 0
  for a in xrange(A):
    for b in xrange(B):
      if a&b < K:
        S += 1
  res = S
      
#  res = -1
#  if (A<K) or (B<K):
#    res = A*B
#  else:
#    res = K*K + (A-K)*K + (B-K)*K
#  print A,B,K

  


  # -------------------------------------------------
  res = 'Case #%d: %d'%(n+1, res)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
