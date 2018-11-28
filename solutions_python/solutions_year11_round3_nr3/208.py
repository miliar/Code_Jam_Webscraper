import sys
import re
import os
import math


def solve():
  
  (N, L, H) = map(int, next(fin).split())
  
  
  freq = map(int, next(fin).split())
  
  
  for x in range(L, H+1):
    found = 1
    for f in freq:
      if f%x == 0 or x%f == 0:
        continue
      else:
        found = 0
        break
    if found == 1:
      break
    
    
      
  if found == 1:
    print>>fout, x
  else:
    print>>fout, "NO"  


if len(sys.argv) != 2:
  print 'specify input file'
  exit()


fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')

numCases = int(next(fin))
for caseNo in range(numCases):
  print>>fout, 'Case #%s:'%(caseNo+1),
  solve()

fin.close()
fout.close()


  
  

