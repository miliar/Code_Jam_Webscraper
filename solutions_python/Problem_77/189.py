#!/usr/bin/python

#
# From: http://en.wikipedia.org/wiki/Cycle_sort
# As this algorithm has the minimum number of writes,
# And Goro spends a mean of 2 hits to swap 2 elements (so 2 writes)
# It mean that, in mean, Goro shall hit the table once per write...
def cycleSort(array):
  writes = 0
 
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
 
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
 
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
      continue
 
    # Otherwise, put the item there or right after any duplicates.
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
 
    # Rotate the rest of the cycle.
    while pos != cycleStart:
 
      # Find where to put the item.
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
 
      # Put the item there or right after any duplicates.
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1
 
  return writes
##

def solve(fd):
    N = int(fd.readline().strip('\n'))
    Values = [ int(x)-1 for x in fd.readline().split() ]
    cs = cycleSort(list(Values))
    return "%.6f" % (cs)
        

import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = int(fd.readline().strip('\n'))
for i in xrange(T):
    print("Case #%d: %s" % (i+1, solve(fd)))

fd.close()
