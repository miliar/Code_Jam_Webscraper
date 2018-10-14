from sys import stdin
import numpy as np


lines = stdin.readlines()
lines.pop(0)

for i,l in enumerate(lines):
  l = map(int,l.split())
  s,p = (l[1],l[2])
  ret = l[0]
  l=np.array(l[3:])
  if p >= 2 :
    a = len(np.where(l >= (3*p-2))[0]) 
    b = len(np.where(l >= (3*p-4))[0])
    ret= a + min(b-a,s)
  elif p == 1:
    ret = len(np.where(l > 0)[0]) 
  print "Case #%d: %d" % (i+1, ret)

