class Cell:
  def __init__(self, altitude):
    self.up = []
    self.down = None
    self.basin = None
    self.altitude = altitude

  def getbasin(self):
    if self.down == None:
      return self
    else:
      return self.down.getbasin()
  def setbasin(self, c):
    self.basin = c
    for ancestor in self.up:
      ancestor.setbasin(c)

T = int(raw_input())
for i in xrange(1, T+1):
  H, W = map(int, raw_input().split())
  grid = []
  for row in xrange(H):
    grid.append([])
    for altitude in map(int, raw_input().split()):
      grid[row].append(Cell(altitude))
  for row in xrange(H):
    for col in xrange(W):
      minnode = None
      minalt = grid[row][col].altitude
      if row < H-1:
        if grid[row+1][col].altitude <= minalt:
          minnode = grid[row+1][col]
          minalt = grid[row+1][col].altitude
      if col < W-1:
        if grid[row][col+1].altitude <= minalt:
          minnode = grid[row][col+1]
          minalt = grid[row][col+1].altitude
      if col > 0:
        if grid[row][col-1].altitude <= minalt:
          minnode = grid[row][col-1]
          minalt = grid[row][col-1].altitude
      if row > 0:
        if grid[row-1][col].altitude <= minalt:
          minnode = grid[row-1][col]
          minalt = grid[row-1][col].altitude

      if minalt < grid[row][col].altitude:
        grid[row][col].down = minnode
        minnode.up.append(grid[row][col])
  print "Case #"+str(T)+":"
  basinlabel = 'a'
  for row in xrange(H):
    for col in xrange(W):
      if not grid[row][col].basin:
        basin = grid[row][col].getbasin()
        basin.setbasin(basinlabel)
        basinlabel = chr(ord(basinlabel)+1)
      print grid[row][col].basin,
    print

