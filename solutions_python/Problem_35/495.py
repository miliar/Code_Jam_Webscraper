import os
import re
from sys import *

def isLocalMinimum(map, i, j, h, w):
  x = map[i][j]
  if j>0  and map[i][j-1]<x:
    return False
  if j<w-1 and map[i][j+1]<x:
    return False
  if i>0 and map[i-1][j]<x:
    return False
  if i<h-1  and map[i+1][j]<x:
    return False
  return True

def getDirection(map, i, j, h, w):
  m = None
  r =''
  if i>0 and (m is None or map[i-1][j]<m):
    r = 'N'
    m = map[i-1][j]
  if j>0  and (m is None or  map[i][j-1]<m):
    r = 'W'
    m = map[i][j-1]
  if j<w-1 and (m is None or map[i][j+1]<m):
    r =  'E'
    m = map[i][j+1]
  if i<h-1  and (m is None or map[i+1][j]<m):
    r = 'S'
    m = map[i+1][j]
  return r


infile = open(argv[1],"r")
outfile = open(argv[1] + "out","w")
line = infile.readline()

T = int(line.split()[0])
abc=[chr(x) for x in range(97, 123)]

for k in range(0,T):
  line = infile.readline()
  H = int(line.split()[0])
  W = int(line.split()[1])
  map = []
  wshed = []
  wshed2 = []
  for i in range(0,H):
    line = infile.readline()
    map = map + [[int (x) for x in line.split()]]
    wshed2 = wshed2 + [[' ' for x in line.split()]]
    wshed = wshed + [[' ' for x in line.split()]]

  alphabet = 0
  for i in range(0,H):
    for j in range(0,W):
      if isLocalMinimum(map, i, j, H,W):
        wshed[i][j] = abc[alphabet]
        alphabet += 1
      else:
        wshed[i][j] = getDirection(map, i, j, H, W)
  changes = -1
  while changes != 0:
    changes = 0
    for i in range(0,H):
      for j in range(0,W):
        e=wshed[i][j]
        if not e in abc:
          if e=='N' and wshed[i-1][j] in abc:
            wshed[i][j] = wshed[i-1][j]
            changes +=1
          if e=='E' and wshed[i][j+1] in abc:
            wshed[i][j] = wshed[i][j+1]
            changes +=1
          if e=='W' and wshed[i][j-1] in abc:
            wshed[i][j] = wshed[i][j-1]
            changes +=1
          if e=='S' and wshed[i+1][j] in abc:
            wshed[i][j] = wshed[i+1][j]
            changes +=1
  writes =-1
  alphabet = 0
  while writes != 0:
    writes = 0
    letter = 'N'
    newletter = 'N'
    b = False
    for i in range(0,H):
      if b: break
      for j in range(0,W):
        if wshed[i][j] != '':
          letter =wshed[i][j];
          newletter = abc[alphabet]
          alphabet+=1
          b = True
          break
    for i in range(0,H):
      for j in range(0,W):
        if wshed[i][j] == letter:
          wshed[i][j] = ''
          wshed2[i][j] = newletter
          writes +=1


  outfile.write ('Case #' + str(k+1) + ':\n')
  for i in range(0,H):
    for j in range(0,W):
       outfile.write (wshed2[i][j] )
       if (j<W-1): outfile.write (' ' )
    outfile.write ('\n')
outfile.close()



