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
def get_sol(N):

	D = []
	while N > 0:
		D = [N%10] + D
		N = (N/10)

	if len(D) == 1:
		return D[0]
	else:
		ready = False
		while not ready:
			p = len(D)-1
			while p>=1 and D[p-1] <= D[p]:
				p -= 1
			if p == 0:
				ready = True
			else:
				while D[p-1] == 0:
					p -= 1
				D[p-1] -= 1
				k = p
				while k < len(D):
					D[k] = 9
					k += 1

		D.reverse()
		N = sum([x*(10**k) for k,x in enumerate(D)])
		return N


#---------------------------------------------------------------------
# Main
ncases = int(lines[0])
lines  = lines[1:]
for ncase in xrange(ncases):
  data  = int(lines[0])
  lines = lines[1:]

  solution = get_sol(data)

  # -------------------------------------------------
  res = 'Case #%d: %s'%(ncase+1, solution)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
