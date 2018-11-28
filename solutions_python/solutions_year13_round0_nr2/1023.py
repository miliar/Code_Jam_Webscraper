f = open('B-large.in', 'r')
fo = open('B-large.out', 'w')
def ip():
  global f
  return f.readline()

def op(st):
  global fo
  fo.write(st + "\n")
  
def grass_possible(x, y, grid):
  num = grid[y][x]
  vert_test = True
  for row in xrange(0, y):
    if grid[row][x] > num:
      vert_test = False
  for row in xrange(y+1, len(grid)):
    if grid[row][x] > num:
       vert_test = False
  if vert_test:
    return True
  hor_test = True
  for col in xrange(0, x):
    if grid[y][col] > num:
      hor_test = False
  for col in xrange(x+1, len(grid[0])):
    if grid[y][col] > num:
      hor_test = False
  if hor_test:
    return True
  return False
  
num_cases = int(ip())

for case in xrange(num_cases):
  rows, cols = [int(num) for num in ip().split(' ')]
  grid = []
  for row in xrange(rows):
    grid.append([int(num) for num in ip().split(' ')])
  should_break = False
  for x in xrange(cols):
    for y in xrange(rows):
      if not grass_possible(x,y,grid):
        should_break = True
        break
    if should_break:
      break
  op("Case #%d: %s" % (case+1, "NO" if should_break else "YES"))