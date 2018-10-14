#!/usr/bin/env python

def ri():
  x = ''
  while not x:
    x = raw_input().strip()
  return x

def Cost(a,b,p):
  return p*((b-a)*N-(b-a)*(b-a-1)/2)

T = int(ri())
for t in xrange(1,T+1):
  N,M = map(int,ri().split())
  x = []
  cost = 0
  for i in xrange(M):
    a,b,p = map(int,ri().split())
    x.append((a,-p))
    x.append((b,p))
    cost += Cost(a,b,p)
  x.sort()
  s = []
  best = 0
  for pos,cnt in x:
    if cnt<0: #start
      s.append((pos,-cnt))
    else:
      while s and cnt >= s[-1][1]:
        lastpos,lastcnt = s.pop()
        best += Cost(lastpos,pos,lastcnt)
        cnt -= lastcnt
      if s and cnt:
        lastpos,lastcnt = s.pop()
        best += Cost(lastpos,pos,cnt)
        s.append((lastpos,lastcnt-cnt))
  print 'Case #%d:'%t, cost-best
      


