from __future__ import division
import sys
import time

fin = sys.stdin
fout = open('c.out','w')
T = int(fin.readline())
for case in range(1,T+1):
  a = fin.readline()
  temp = map(int,a.split())
  N = temp[0]
  L = temp[1]
  H = temp[2]
  b = fin.readline()
  others = map(int,b.split())
  note = 0
  found = False
  for i in range(L,H+1):
    found = True
    for j in others:
      if i > j:
        if i%j != 0:
          found = False
          break
      elif j > i:
        if j%i != 0:
          found = False
          break
    if found == True:
      note = i
      break
  if found:
    fout.write("Case #{0}: {1}\n".format(case,note))
  else:
    fout.write("Case #{0}: {1}\n".format(case,'NO'))
fout.close


