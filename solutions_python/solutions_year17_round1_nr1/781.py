import numpy as np
def printOut(I, p):
  print "Case #{}: {}".format(I, p)

t = int(raw_input())
for I in xrange(1, t + 1):
  R, C = [int(s) for s in raw_input().split(" ")]

  print "Case #{}:".format(I)


  grid = []
  for i in xrange(0, R):
    grid.append(list(raw_input()))


  for j in xrange(0, R):

    # left to right
    i = 0
    shouldContinue = 0
    while  i<C and grid[j][i]=='?':
      i += 1
    if i >= C:
      continue

    while i < C-1:
      if grid[j][i+1]=='?':
        grid[j][i+1] = grid[j][i]
      i += 1

    # right to left
    i = C-1
    while i>=0 and grid[j][i]=='?':
      i -= 1
    if i < 0:
      continue

    while i > 0:
      if grid[j][i-1]=='?':
        grid[j][i-1] = grid[j][i]
      i -= 1


  for j in xrange(0, R):
    while j < R and grid[j][0]=='?':
      j += 1
    if j == R and not grid[j-1][0]=='?':
      continue
    j = j-1
    if j == R-1 and grid[j][0]=='?':
      j -= 1
      while grid[j][0]=='?':
        j -= 1
      j += 1
      while j < R:
        grid[j] = grid[j-1]
        j += 1
    elif j < 0:
      continue
    else:
      while grid[j][0]=='?':
        grid[j] = grid[j+1]
        j -= 1

  for i in xrange(0, R):
    print ''.join(grid[i])






