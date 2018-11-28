#!/usr/bin/python
import sys, math

T = int(sys.stdin.readline())
IMP = 'Impossible'
for t in range(T):
  print "Case #%d:" % (t + 1)
  R, C = map(int, sys.stdin.readline().split())
  m = [[]]*R
  count = 0
  for r in range(R):
    l = sys.stdin.readline().strip()
    row = [0]*C
    for c in range(C):
      if l[c] == '#':
        row[c] = 1
        count += 1
      else:
        row[c] = '.'
    m[r] = row
      
  possible = True
  for r in range(R):
    for c in range(C):
      if m[r][c] == 1:
        if r < R-1 and c < C-1 and m[r][c+1] == 1 and m[r+1][c] == 1 and m[r+1][c+1] == 1:
          m[r][c] = '/'
          m[r][c+1] = '\\'
          m[r+1][c] = '\\'
          m[r+1][c+1] = '/'
          count -= 4
        else:
          possible = False
          break
    if not possible:
      break
  
  if possible and count == 0:
    for r in range(R):
      print ''.join(m[r])
  else:
    print IMP
