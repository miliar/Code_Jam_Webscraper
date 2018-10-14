#!/usr/bin/python
import sys

def f(v,ix,k):
  n, i, s = len(v), 0, 0
  while i<n and s+v[(ix+i)%n]<=k:
    s += v[(ix+i)%n]
    i +=1
  return ((ix+i)%n, s)

def loop(gs,mm):
  p = 0
  q = [p]
  while mm[p][0] not in q:
    p = mm[p][0]
 #   print "now in ",p
    q.append(p)
  p = mm[p][0]
  q = q[q.index(p):]
#  print "end in ",p,q
  return (p, len(q), sum([mm[ix][1] for ix in q]))

data = [map(int,l.strip().split(' ')) for l in sys.stdin if l.strip()!=""][1:]
for t in range(len(data)/2):
  R, k = data[t*2][0], data[t*2][1]
#  print R,k
  gs = data[t*2+1]
  mm = [f(gs,i,k) for i in range(len(gs))]
  
#  print "groups:",gs
#  print "mm:",mm

  lix, llen, leu = loop(gs,mm)
#  print "loop starts at ",lix,"with length",llen,"costs",leu

  eu, p = 0, 0
  while R>0 and p!=lix:
    p, m = mm[p]
    R -= 1
    eu += m

#  print "after head, R=",R," eu=",eu

  loops = R//llen
  R -= llen*loops
  eu += leu*loops

  while R>0:
    p, m = mm[p]
    R -= 1
    eu += m

#  print "after mid loop, R=",R," eu=",eu

#  print "*",(R,k,gs),eu

  print "Case #%d: %s" % (t+1, eu)

