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
def get_sol(K,S):

  ns  = len(S)
  n   = 0
  sol = 0
  while n < ns:
    if S[n] == 0:
      if n+K-1 < ns:
        sol += 1
        for m in xrange(K):
          S[n+m] = (S[n+m]+1)%2
      else:
        sol = 'IMPOSSIBLE'
        break
    n += 1

  return str(sol)

#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  data  = lines[0].split()
  lines = lines[1:]
  K  = int(data[1])
  S  = [int(c=='+') for c in data[0]]
  S1 = [x for x in S]
  S.reverse()
  S2 = S
  solution1 = get_sol(K,S1)
  solution2 = get_sol(K,S2)
  if solution1 == solution2:
    solution = solution1
  else:
    print 'Error: ', solution1, solution2
    exit(0)


  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
