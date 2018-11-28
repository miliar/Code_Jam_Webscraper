#!/bin/env python

cases = int(raw_input())

for i in xrange(cases):
  R, C = map(int, raw_input().split())
  rows = []
  for r in xrange(R):
    rows.append(raw_input().strip())
  
  done = []
  pos = []
  for r in range(R):
    done.append([False] * C)
    pos.append([False] * C)
  

  for r in range(R):
    row = False
    for c in range(C):
      if rows[r][c] == '.':
        continue
      if row:
        pos[r][c] = True
      if rows[r][c] == '<' and row:
        done[r][c] = True
      row = True

  for r in range(R):
    row = False
    for c in range(C)[::-1]:
      if rows[r][c] == '.':
        continue
      if row:
        pos[r][c] = True
      if rows[r][c] == '>' and row:
        done[r][c] = True
      row = True

  for c in range(C):
    row = False
    for r in range(R):
      if rows[r][c] == '.':
        continue
      if row:
        pos[r][c] = True
      if rows[r][c] == '^' and row:
        done[r][c] = True
      row = True

  ans = 0
  impos = False

  for c in range(C):
    row = False
    for r in range(R)[::-1]:
      if rows[r][c] == '.':
        continue
      if row:
        pos[r][c] = True
      if rows[r][c] == 'v' and row:
        done[r][c] = True
      row = True
      if not done[r][c]:
        ans += 1
      if not pos[r][c]:
        impos = True

  if impos:
    ans = "IMPOSSIBLE"
  print "Case #{}: {}".format(i+1, ans)
