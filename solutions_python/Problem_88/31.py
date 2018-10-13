import time

data = [l.strip() for l in open("B-small.in", "r").readlines()]
out = open("B-small.out", "w")  

def check(grid, posssize, startrow, startcol):
  rcom = startrow + ((posssize - 1.0) / 2.0)
  ccom = startcol + ((posssize - 1.0) / 2.0)
  rdev = 0
  cdev = 0
  for rr in range(startrow, startrow + posssize):
    for cc in range(startcol, startcol + posssize):
      corner = False
      if rr == startrow or rr == startrow + posssize - 1:
        if cc == startcol or cc == startcol + posssize - 1:
          corner = True
      if not corner:
        rdev += (d + grid[rr][cc]) * (rr - rcom)
        cdev += (d + grid[rr][cc]) * (cc - ccom)
  if rdev == 0 and cdev == 0:
    return True
  else:
    return False

ncases = int(data.pop(0))
for case in range(ncases):
  r, c, d = [int(i) for i in data.pop(0).split(' ')]
  grid = []
  for i in range(r):
    newrow = []
    row = data.pop(0)
    for l in row:
      newrow.append(int(l))
    grid.append(newrow)
  bestsize = 'IMPOSSIBLE'
  for posssize in range(3, min(r, c) + 1):
    for startrow in range(0, r - posssize + 1):
      for startcol in range(0, c - posssize + 1):
        if check(grid, posssize, startrow, startcol):
          bestsize = posssize 
  out.write("Case #" + str(case+1) + ": " + str(bestsize) + "\n")
 
