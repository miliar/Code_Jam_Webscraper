#!/usr/bin/python

import collections

rl = raw_input

T = int(rl())

def ff(m,l,r,c,H,W,hack):
  best = (0,0)
  v = m[r][c]
  if l[r][c] != -1:
    return l[r][c]
  for dr,dc in [(-1,0),(0,-1),(0,1),(1,0)]:
    if 0 <= r+dr < H and 0 <= c+dc < W and m[r+dr][c+dc] < v:
      best = (dr,dc)
      v = m[r+dr][c+dc]
  if best == (0,0):
    l[r][c] = hack[0]
    hack[0] += 1
    return l[r][c]
  l[r][c] = ff(m,l,r+best[0],c+best[1],H,W,hack)
  return l[r][c]

for x in xrange(1,T+1):
  H,W = map(int,rl().split())
  m = list()
  l = list(list(-1 for c in xrange(W)) for r in xrange(H))
  for r in xrange(H):
    m.append(map(int,rl().split()))
  hack = [0]
  for r in xrange(H):
    for c in xrange(W):
      ff(m,l,r,c,H,W,hack)
  print "Case #%d:" % x
  for r in xrange(H):
    print " ".join(chr(ord("a")+l[r][c]) for c in xrange(W))


