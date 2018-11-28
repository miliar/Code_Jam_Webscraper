#!/usr/bin/python2.5

import sys

def GetNextBasin(current_basin):
  return chr(ord(current_basin) + 1)

def FindFlowDestination(map, x, y):
  neighbors = []
  if y > 0: # north
    neighbors.append((x, y - 1, map[y - 1][x]))
  if x > 0: # west
    neighbors.append((x - 1, y, map[y][x - 1]))
  if x < len(map[0]) - 1: # east
    neighbors.append((x + 1, y, map[y][x + 1]))
  if y < len(map) - 1: # south
    neighbors.append((x, y + 1, map[y + 1][x]))

  if not neighbors:
    return None

  minimum = min(n[2] for n in neighbors)
  minimums = tuple(n for n in neighbors if n[2] == minimum)

  if minimum < map[y][x]: # some neighbors are lower than us
    return (minimums[0][0], minimums[0][1])
  else:
    return None # we don't flow anywhere


def LetTheLoveFlow(map, basins, x, y, next_basin):
  if basins[y][x]:
    return next_basin # we already flowed through here
  basins[y][x] = next_basin
  trace = []

  while True:
    trace.append((x, y))
    destination = FindFlowDestination(map, x, y)
    if not destination:
      # sink, we're done
      return GetNextBasin(next_basin)
    else:
      x, y = destination
      if basins[y][x]:
        # we entered another flow, traceback and re-label
        for t in trace:
          basins[t[1]][t[0]] = basins[y][x]
        return next_basin
      else:
        # another un-assigned flow, let's just go there and mark it
        basins[y][x] = next_basin


T = int(sys.stdin.readline())
for t in xrange(T):
  H, W = (int(x) for x in sys.stdin.readline().split())
  map = tuple(tuple(int(x) for x in sys.stdin.readline().split()) for row in xrange(H))
  basins = list(list(None for x in xrange(W)) for y in xrange(H))

  next_basin = 'a'
  for y in xrange(H):
    for x in xrange(W):
      next_basin = LetTheLoveFlow(map, basins, x, y, next_basin)

  print "Case #%d:" % (t + 1)
  print "\n".join(" ".join(row) for row in basins)
