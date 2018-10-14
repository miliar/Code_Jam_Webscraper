#!/usr/bin/python
import sys
from fractions import gcd

data = [l.strip().split(' ') for l in sys.stdin if l.strip()!=""][1:]
data = [[int(tok) for tok in v if tok!=''][1:] for v in data]
#print data

for c in range(len(data)):
  v = data[c]
  v.sort()
  t = v[len(v)-1]-v[0]
#  print "init t",t
  for i in range(len(v)-2,0,-1):
    t = gcd(t, v[i]-v[0])
#  print "last t",t

  r = (v[0]+(t-1))//t*t-v[0]
  print "Case #%d: %d" % (c+1, r)

