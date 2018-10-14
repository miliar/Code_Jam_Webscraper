#!/usr/bin/env python

import sys

INF = 10000000

def next_char(c):
  return chr(ord(c)+1)

T = int(raw_input())

def neighbour(i, j):
  global height, H, W, case
  lowest = (height[i][j], None)
  for d in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
    if height[i+d[0]][j+d[1]] < lowest[0]:
      lowest = (height[i+d[0]][j+d[1]], d)
  return lowest[1]

for case in xrange(1, T+1):
  print "Case #%d:" % case
  H, W = map(int, raw_input().split())
  height = [[INF] * (W+2)] + [[INF] + map(int, raw_input().split()) + [INF] for i in xrange(H)] + [[INF] * (W+2)]
  mp = [[None] * (W+2) for i in xrange(H+2)]
  next = 'a'
  change = True
  while change:
    change = False
    for i in xrange(1, H+1):
      for j in xrange(1, W+1):
        if mp[i][j] != None:
          continue
        neigh = neighbour(i, j)
        change = True
        if neigh == None:
          mp[i][j], next = next, next_char(next)
        else:
          mp[i][j] = mp[i+neigh[0]][j+neigh[1]]
        lowest = (height[i][j], None)
  next = 'a'
  translate = {}
  for i in xrange(1, H+1):
    for j in xrange(1, W+1):
      if mp[i][j] not in translate.keys():
        translate[mp[i][j]], next = next, next_char(next)
  for i in xrange(1, H+1):
    print " ".join(map(lambda x: translate[x], mp[i][1:W+1]))
