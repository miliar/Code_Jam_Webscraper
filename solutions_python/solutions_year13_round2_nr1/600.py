import sys 
import string
from collections import *

f = open(sys.argv[1])

T = int(f.readline())
for c in xrange(1, T+1): 
   line = f.readline().strip().split(' ')
   A = int(line[0])
   N = int(line[1])
   line = f.readline().strip().split(' ')
   motes = list()
   for m in line:
     motes.append(int(m))
   motes = sorted(motes)
   ops = 0
   tr = 0
   while len(motes)>0:
      if A == 1:
         ops = len(motes)
         motes = list()
      elif A<=motes[0]:
         #print 'added mote ' + str(A-1)
         ops += 1
         if tr<len(motes):
           #print str(A) + 'ate ' + str(A-1)
           A = A+(A-1)
           tr += 1
         else:
           #print 'deleted ' + str(tr) + ' motes'
           ops = ops - 1 - (len(motes) - tr)
           motes = list()
      else:
         #print str(A) + 'ate ' + str(motes[0])
         A = A + motes[0]
         del motes[0]
         tr = 0
   print 'Case #' + str(c) + ': ' + str(ops)

