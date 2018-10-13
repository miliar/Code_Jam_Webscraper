#!/usr/bin/python

# Solution to watershed problem
# Googld Code Jam, 2009 Qualification round
# Alex Roper <alexr@ugcs.caltech.edu>
# California Institute of Technology

# Basic approach: first find and label the sinks. Then, starting at them,
# spiral out similar to A* and enqueue their neighbors and use neighbor rules.
# We're looking at O(N) in map area, I believe.

import sys, collections, numpy

def read_tokens(f):
  for line in f:
    for t in line.split():
      yield t

def append_inner_g(todo, (i, j), (h, w), shed):
  if 0 < i < h - 1 and 0 < j < w - 1 and not shed[i, j]: todo.append((i, j))

def adjacent(i, j):
  return (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)

def solve(rdr):
  h, w = [int(rdr()) for _ in range(2)]
  alt = [[int(rdr()) for x in range(w)] for y in range(h)]

  # Pad the maps on all four sides with mountains to make edge cases easier.
  h += 2; w += 2
  alt = [[20000] * w] + [[20000] + r + [20000] for r in alt] + [[20000] * w]
  alt = numpy.matrix(alt)
  shed = numpy.matrix([[None] * w] * h)

  # First step: Find the sinks. We index from one for truth reasons. Also
  # mark their neighbors for the start of our labeling phase.
  nextshed = 1
  todo = collections.deque()
  append_inner = lambda (i, j): append_inner_g(todo, (i, j), (h, w), shed)
  for i in range(1, h - 1):
    for j in range(1, w - 1):
      if alt[i,j] <= min(alt[i-1,j], alt[i+1,j], alt[i,j+1], alt[i,j-1]):
        shed[i,j] = nextshed
        nextshed += 1
        map(append_inner, adjacent(i, j))

  # Second step: Label all cells that aren't sinks.
  while todo:
    i, j = todo.popleft()
    if not shed[i, j]:
      adj = adjacent(i, j)
      neigh = map(alt.item, adj)
      # If there's a tie, choose the first on ein priority list.
      into = adj[neigh.index(min(neigh))]
      # If it's labeled, get it. Otherwise, wait until we hit it from another sink.
      if shed.item(into):
        shed[i, j] = shed.item(into)
        map(append_inner, adjacent(i, j))

  # Output answer, as we go building the rename dict
  rdict = {}
  cv = ord('a')
  for i in range(1, h - 1):
    for j in range(1, w - 1):
      if shed[i, j] not in rdict:
        rdict[shed[i, j]] = cv
        cv += 1
      print chr(rdict[shed[i, j]]),
    print ""

def main():
  # Read specs
  rdr = read_tokens(open(sys.argv[1])).next
  T = int(rdr())
  for c in range(T):
    print "Case #%i:" % (c + 1)
    solve(rdr)

if __name__ == "__main__": main()
