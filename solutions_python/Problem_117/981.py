#!/usr/bin/env python

import sys

#convert = {'O': , 'X':, '.': , 'T':}

def debugprint(arr):
  for l in arr:
    print " ".join(map(lambda x : str(x).ljust(3), l))

def calc(arr):
  for y, l in enumerate(arr):
    for x, v in enumerate(l):
      # check the whole x and the whole y row if its possible to delete.
      # if both not possible return NO
      # if both possible skip 
      if v < 0:
        continue

      # first check x 
      vertical = True
      for row in arr:
        if abs(row[x]) > v:
          vertical = False
      # then check y
      horizontal = True
      for col in l:
        if abs(col) > v:
          horizontal = False
      if vertical:
        for yy in range(len(arr)):
          if arr[yy][x] == v:
            arr[yy][x] = -v
      if horizontal:
        for xx in range(len(arr[y])):
          if arr[y][xx] == v:
            arr[y][xx] = -v
      if not vertical and not horizontal:
        return "NO"
  for y, l in enumerate(arr):
    for x, v in enumerate(l):
      if v >= 0:
        return "NO"
  return "YES"

  

      
def get_array(ifile):
  n,m = ifile.readline().strip().split(' ')
  return [map(lambda x: int(x), ifile.readline().strip().split(' ')) for i in range(int(n))]

ifile = open(sys.argv[1])
if len(sys.argv) > 2:
  ofile = open(sys.argv[2])
else:
  ofile = sys.stdout
for i in range(int(ifile.readline().strip())):
  #if i == 9:
  #  import ipdb; ipdb.set_trace()
  print "Case #%i: %s" % (i+1, calc(get_array(ifile)))
