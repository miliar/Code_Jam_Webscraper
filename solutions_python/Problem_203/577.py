def answer(grid):
  rows = len(grid)
  cols = len(grid[0])
  # fill left & right
  for row in range(rows):
    curr = None
    for col in range(cols):
      cell = grid[row][col]
      if cell != '?' and curr != cell:
        if curr is None:
          # fill left because it is all '?'
          for xcol in range(col):
            grid[row][xcol] = cell
        curr = cell
      elif curr is not None:
        grid[row][col] = curr
  # fill up & down
  for row in range(rows):
    if grid[row][0] == '?':
      continue
    curr = grid[row][0]
    x = 0
    for col in range(cols):
      cell = grid[row][col]
      if curr != cell:
        # fill up
        fill(curr, row, col - 1, x - 1, -1, lambda y: y >= 0, grid)
        # fill down
        fill(curr, row, col - 1, x - 1, 1, lambda y: y < rows, grid)
        curr = cell
        x = 1
      else:
        x += 1
    # fill up
    fill(curr, row, col, x - 1, -1, lambda y: y >= 0, grid)
    # fill down
    fill(curr, row, col, x - 1, 1, lambda y: y < rows, grid)
  return grid

def fill(curr, row, col, width, direction, not_of_bounds, grid):
  y = direction
  filling = True
  while not_of_bounds(row + y):
    x = width
    while x >= 0:
      # print('cc', grid[row + y][col - x - 1])
      if grid[row + y][col - x] != '?':
        filling = False
        break
      x -= 1
    if not filling:
      break
    x = width
    while x >= 0:
      grid[row + y][col - x] = curr
      x -= 1
    y += direction

t = int(input())
for i in range(1, t+1):
  r, c = [int(s) for s in input().split(' ')]
  grid = [list(input()) for ri in range(r)]
  result = answer(grid)
  print('CASE #' + str(i) + ':')
  for row in result:
    print(''.join(row))
