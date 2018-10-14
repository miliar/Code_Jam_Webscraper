import sys
filename = 'input.txt'
if len(sys.argv) > 1:
  filename = sys.argv[1]
f = open(filename)
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]

def get_next(grid):
  for x, row in enumerate(grid):
    for y, cell in enumerate(row):
      if cell == '#':
        return x,y
  return -1, -1

def can_color(grid, x, y):
  tl = x,y, '/'
  tr = x+1,y, '\\'
  bl = x,y+1, '\\'
  br = x+1,y+1, '/'
  for i,j, ch in (tl,tr,bl,br):
    if i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '#':
      return False, grid
    else:
      grid[i][j]=ch
  return True, grid

def pretty(grid):
  rows = [''.join(row) for row in grid]
  return '\n'.join(rows)

def solve(grid):
  x,y = get_next(grid)
  while x > -1:
    yes, grid = can_color(grid, x, y)
    if not yes:
      return 'Impossible'
    x,y = get_next(grid)
  return pretty(grid)

N = int(lines[0])
lines = lines[1:]
for i in range(N):
  dims = lines[0]
  lines = lines[1:]
  height = int(dims.split(' ')[0])
  grid = lines[:height]
  lines = lines[height:]
  grid = [[x for x in row] for row in grid]

  soln = solve(grid)
  print "Case #%s:" % (i+1)
  print soln
  
