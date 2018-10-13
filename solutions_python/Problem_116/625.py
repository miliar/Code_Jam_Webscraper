import sys

T = int(sys.stdin.readline().strip())

def get_result(grid):
  # so ugly :(

  def check(x,y,vertical=True):
    piece = grid[y][x]
    cnt = 1
    if piece == '.':
      return False
    if piece == 'T':
      if vertical:
        y += 1
      else: 
        x += 1
      p = grid[y][x]
      cnt += 1
    else:
      p = piece
    if vertical:
        y += 1
    else: 
      x += 1
    while y < 4 and x < 4 and p == piece:
      p = grid[y][x] if grid[y][x] != 'T' else piece
      cnt += 1 if p == piece else 0
      if vertical:
        y += 1
      else: 
        x += 1
    if cnt == 4:
      return piece
    return False

  def checkY():
    for x in range(0,4):
      y = 0
      res = check(x,y,vertical=True)
      if res:
        return res
    return False

  def checkX():
    for y in range(0,4):
      x = 0
      res = check(x,y,vertical=False)
      if res:
        return res
    return False

  def checkDiagonals():
    p = grid[0][0] if not grid[0][0] == 'T' else grid[1][1]
    if not p == '.':
      cnt = 1
      for y in range(1,4):
        if grid[y][y] == p or grid[y][y] == 'T':
          cnt+=1
      if cnt == 4:
        return p

    p = grid[0][3] if not grid[0][3] == 'T' else grid[1][2]
    cnt = 1
    if not p == '.':
      for y in range(1,4):
        if grid[y][-y-1] == p or grid[y][-y-1] == 'T':
          cnt+=1
      if cnt == 4:
        return p
    return False

  return checkY(), checkX(), checkDiagonals()

for t in range(0,T):
  grid = []
  for i in range(0,4):
    line = sys.stdin.readline().strip()
    grid.append(line)
  res = get_result(grid)
  sys.stdin.readline()
  result = filter(None, res)
  if result:
    result = result[0] + ' won'
  else:
    if any(['.' in g for g in grid]):
      result = 'Game has not completed'
    else:
      result = 'Draw'
  print "Case #%d: %s" % (t + 1, result)