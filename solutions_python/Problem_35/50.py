#!/usr/bin/env python
import sys

count = raw_input()
N = eval(count)
class PCRelation:
  def __init__(self):
    self.P2C = {}
    self.C2P = {}
  def SetRelation(self, parent, child):
    self.P2C[parent] = child
    self.C2P[child] = parent
  def GetParent(self, child):
    return self.C2P[child]
  def GetChild(self, parent):
    return self.P2C[parent]
  def GetLastChild(self, parent):
    while(self.P2C[parent] != parent):
      parent = self.P2C[parent]
    return parent

for i in range(N):
  mapSize = raw_input()
  mapSize = mapSize.split(' ')
  H = eval(mapSize[0])
  W = eval(mapSize[1])
  mapData = []
  for j in range(H):
    row = raw_input()
    row = row.split(' ')
    mapData += [row]
  mapInts = {}
  for x in range(W):
    for y in range(H):
      mapInts[(x,y)] = [eval(mapData[y][x])]
  relation = PCRelation()
  for x in range(W):
    for y in range(H):
      child = (x,y)
      if(y>0):
        if(mapInts[(x,y-1)] < mapInts[child]):
          child = (x,y-1)
      if(x>0):
        if(mapInts[(x-1,y)] < mapInts[child]):
          child = (x-1,y)
      if(x<W-1):
        if(mapInts[(x+1,y)] < mapInts[child]):
          child = (x+1,y)
      if(y<H-1):
        if(mapInts[(x,y+1)] < mapInts[child]):
          child = (x,y+1)
      relation.SetRelation((x,y), child)
  
  mapSinks = {}
  
  mapSinkCount = 0
  for y in range(H):
    for x in range(W):
      parent = (x,y)
      child = relation.GetLastChild(parent)
      if(mapSinks.has_key(child)):
        mapSinks[parent] = mapSinks[child]
      else:
        mapSinks[child] = chr(97+mapSinkCount)
        mapSinks[parent] = mapSinks[child]
        mapSinkCount += 1
  for x in range(W):
    for y in range(H):
      parent = (x,y)
      child = relation.GetLastChild(parent)
      mapSinks[parent] = mapSinks[child]
  
  print "Case #%d:" % (i+1)
  for y in range(H):
    for x in range(W):
      if(x==W-1):
        print mapSinks[(x,y)]
      else:
        print mapSinks[(x,y)],
  