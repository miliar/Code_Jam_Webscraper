import sys

inputFile = sys.stdin
count = int(inputFile.readline())

lineno = 1
for cou in xrange(count):
  R, C = map(int, inputFile.readline().split())

  grid = {}
  for r in xrange(R):
    grid[r] = list(inputFile.readline())

  for r in xrange(R-1):
    for c in xrange(C-1):
      if grid[r][c] == '#' and grid[r+1][c] == '#' and grid[r][c+1] == '#' and grid[r+1][c+1] == '#':
        grid[r][c] = '/'
        grid[r+1][c] = '\\'
        grid[r][c+1] = '\\'
        grid[r+1][c+1] = '/'

  good = True
  for r in xrange(R):
    for c in xrange(C):
      if grid[r][c] == '#':
        good = False

  print "Case #%d:" % lineno

  if good:
    for r in xrange(R):
      print ''.join(grid[r]),
  else:
    print 'Impossible'


  lineno += 1
