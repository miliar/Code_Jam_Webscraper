#!/usr/bin/python
import sys
from sets import Set

f = sys.stdin
N = int(f.readline())
inf = 99999
dh = [-1, 0, 0, 1]
dw = [ 0,-1, 1, 0]

def dfs(h,w):
  global b,e,col
  if b[h][w] != ' ':
    return
  b[h][w] = chr(col)
  for i in e[h][w]:
    dfs(h+dh[i], w+dw[i])

for case in xrange(1, N+1):
  col = 96
  s = f.readline().split()
  H, W = int(s[0]), int(s[1])
  m = [(W+2)*[inf]]
  b = [(W+2)*[' ']]
  e = [(W+2)*[Set()]]
  for h in xrange(0,H):
    m.append([inf]+f.readline().split()+[inf])
    b.append((W+2)*[' '])
    e.append((W+2)*[Set()])
    for w in xrange(1,W+1):
      m[-1][w] = int(m[-1][w])
  m.append((W+2)*[inf])
  b.append((W+2)*[' '])
  e.append((W+2)*[Set()])

  for h in xrange(1,H+1):
    for w in xrange(1,W+1):
      min = 0
      for i in xrange(1,4):
        if m[h+dh[i]][w+dw[i]] < m[h+dh[min]][w+dw[min]]:
          min = i
      if m[h+dh[min]][w+dw[min]] < m[h][w]:
        e[h][w] = Set([min])
      else:
        e[h][w] = Set()

  for h in xrange(1,H+1):
    for w in xrange(1,W+1):
      for i in xrange(0,4):
        if 3-i in e[h+dh[i]][w+dw[i]]:
          e[h][w].add(i)

  for h in xrange(1,H+1):
    for w in xrange(1,W+1):
      if b[h][w] == ' ':
        col += 1
        dfs(h, w)
      
  print 'Case #%d:' % case
  for h in xrange(1,H+1):
    print " ".join(b[h][1:-1])

