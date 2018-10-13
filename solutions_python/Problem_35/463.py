#!/usr/bin/env python
# (c) Christoph Grenz

from sys import stdin, stdout, stderr
from copy import copy

ELEVATION, BASINID = 0, 1

FLOWS = ((-1,0), (0,-1), (0,1), (1,0))

mapcount = int(stdin.readline().strip())

def idGenerator(start='a'):
  i = ord(start)
  while True:
    yield chr(i)
    i+=1

def simulateFlow(map,y,x,cell,ids):
  if cell[BASINID] is not None:
    return cell[BASINID]
  h,w = len(map), len(map[0])
  neighbors = [ (y+dy,x+dx) for dy,dx in FLOWS if 0 <= y+dy < h and 0 <= x+dx < w ]
  next = None
  for (y2,x2) in neighbors:
    n = map[y2][x2]
    if n[ELEVATION] < cell[ELEVATION]:
      if next is None or next[0][ELEVATION] > n[ELEVATION]:
        next = (n,y2,x2);
  if (next):
    basinid = simulateFlow(map,next[1],next[2],next[0],ids)
    cell[BASINID] = basinid
    return basinid
  else:
    cell[BASINID] = ids.next()
    return cell[BASINID]

def checkMap(map):
  if len(map) == 0:
    return
  ids = idGenerator()
  h = len(map)
  w = len(map[0])
  for y in xrange(h):
    for x in xrange(w):
      if map[y][x][BASINID] is not None:
        continue
      map[y][x][BASINID] = simulateFlow(map,y,x,map[y][x],ids)

def outputMap(map):
  for row in map:
    for x in row:
      print x[BASINID],
    print ''

for imap in xrange(mapcount):
  map = []
  h, w = ( int(x) for x in stdin.readline().strip().split(' ', 1) )
  for irow in xrange(h):
    row = [ [int(x), None] for x in stdin.readline().strip().split(' ', w-1) ]
    map.append(tuple(row))
  map = tuple(map)

  print 'Case #%i:' % (imap+1)
  checkMap(map)
  outputMap(map)

  del map