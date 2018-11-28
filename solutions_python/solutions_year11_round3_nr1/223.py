import sys
import re
import os
import math


def solve():
  
  (R, C) = map(int, next(fin).split())
  
  rlist = {}
  possible = 1
  for x in range(R):
    rlist[x] = next(fin).strip()
  
    
  for x in range(R-1):
    ind = rlist[x].find('##')
    tmprow = list(rlist[x])
    while ind != -1:
      rowlst = list(rlist[x+1])
      
      if rowlst[ind] == '#' and rowlst[ind + 1] == '#':
        tmprow[ind] = rowlst[ind + 1] = '/'
        tmprow[ind + 1] = rowlst[ind] = '\\'
        rlist[x] = "".join(tmprow)
        rlist[x+1] = "".join(rowlst)
#        print rlist[x], rlist[x+1]
      else:
        possible = 0
        break
      ind = rlist[x].find('##')
    if rlist[x].find('#') != -1:
      possible = 0
      break
  if rlist[R-1].find('#') != -1:
    possible = 0  
  if R == 1 and rlist[0].find('#') != -1:
    possible = 0
     
  if possible == 0:
    print>>fout, "Impossible"
  else:
    for x in range(R):
      print>>fout, rlist[x]  
      

if len(sys.argv) != 2:
  print 'specify input file'
  exit()


fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')

numCases = int(next(fin))
for caseNo in range(numCases):
  print>>fout, 'Case #%s:'%(caseNo+1)
  solve()

fin.close()
fout.close()


  
  

