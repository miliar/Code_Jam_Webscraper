#!/usr/bin/env python
# encoding: utf-8
"""
AlienLanguage.py

Created by Graham Dennis on 2009-09-03.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import getopt


help_message = '''
The help message goes here.
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg

def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
    except getopt.error, msg:
      raise Usage(msg)
    
    # option processing
    for option, value in opts:
      if option == "-v":
        verbose = True
      if option in ("-h", "--help"):
        raise Usage(help_message)
      if option in ("-o", "--output"):
        output = value
  
  except Usage, err:
    print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
    print >> sys.stderr, "\t for help use --help"
    return 2
  
  f = file(args[0])
  N = int(f.readline())
  
  for i in xrange(N):
    H, W = map(int, f.readline().split())
    heightMap = [(height, []) for h in range(H) for height in map(int, f.readline().split())]
    
    # print heightMap
    
    h, w = 0, -1
    for myIdx, (myHeight, myLst) in enumerate(heightMap):
      w += 1
      if w == W:
        w = 0
        h += 1
      neighbourIdxs = []
      # North
      if h > 0: neighbourIdxs.append(myIdx - W)
      # West
      if w > 0: neighbourIdxs.append(myIdx - 1)
      # East
      if w != W-1: neighbourIdxs.append(myIdx + 1)
      # South
      if h != H-1: neighbourIdxs.append(myIdx + W)
      minHeight = myHeight
      flowIdx = myIdx
      # print h, w, neighbourIdxs, minHeight
      for neighbourIdx in neighbourIdxs:
        neighbourHeight, neighbourLst = heightMap[neighbourIdx]
        if neighbourHeight < minHeight:
          minHeight = neighbourHeight
          flowIdx = neighbourIdx
      if flowIdx != myIdx:
        if not flowIdx in myLst: myLst.append(flowIdx)
        neighbourLst = heightMap[flowIdx][1]
        if not myIdx in neighbourLst: neighbourLst.append(myIdx)
      
    # print heightMap
    visited = set()
    groupMap = [None] * (H * W)
    groupNum = 0
    for myIdx, (myHeight, myLst) in enumerate(heightMap):
      if myIdx in visited: continue
      groupMap[myIdx] = groupNum
      nodesToConsider = set(myLst)
      while nodesToConsider:
        idx = nodesToConsider.pop()
        idxNeighbours = heightMap[idx][1]
        groupMap[idx] = groupNum
        visited.add(idx)
        nodesToConsider.update([j for j in idxNeighbours if not j in visited])
      groupNum += 1
    
    print "Case #%i:" % (i + 1)
    h, w = 0, -1
    groupNames = "abcdefghijklmnopqrstuvwxyz"
    for group in groupMap:
      w += 1
      if w == W:
        print
        w = 0
        h += 1
      print groupNames[group],
    print
    # print line, lineList, matches(root, lineList)
    # print "Case #%i: %i" % (i + 1, matches(root, lineList))
  


if __name__ == "__main__":
  sys.exit(main())
