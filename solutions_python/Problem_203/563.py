def cake(G, rows, cols):
  visited = {}

  for r in range(rows):
    for c in range(cols):
      if G[r][c] != '?' and not(visited.has_key(G[r][c])):
        visited[G[r][c]] = True
        max_horizontal(G, G[r][c], r, c, rows, cols)


def max_horizontal(G, initial, r, c, rows, cols):
  counter_right = c
  counter_left = c


  while((counter_right + 1) < cols and G[r][counter_right + 1] == '?'):
    counter_right += 1
    G[r][counter_right] = initial

  while((counter_left - 1) >= 0 and G[r][counter_left - 1] == '?'):
    counter_left -= 1
    G[r][counter_left] = initial

  if r - 1 >= 0 and G[r-1][c] != initial:
    spread_vertical(G, initial, r-1, c, rows, cols, counter_left, counter_right+1)

  if r + 1 < rows and G[r+1][c] != initial:
    spread_vertical(G, initial, r+1, c, rows, cols, counter_left, counter_right+1)

  

def spread_vertical(G, initial, row, col, rows, cols, start, end):
  cover = True

  for i in range(start, end):
    if G[row][i] != '?' and G[row][i] != initial:
      cover = False
      break

  if cover:
    G[row][col] = initial
    spread_horizontal(G, initial, row, col, rows, cols, start, end)

def spread_horizontal(G, initial, row, col, rows, cols, start, end):
  for i in range(start, end):
    if G[row][i] == '?':
      G[row][i] = initial

  if row - 1 >= 0 and G[row-1][col] != initial:
    spread_vertical(G, initial, row-1, col, rows, cols, start, end)

  if row + 1 < rows and G[row+1][col] != initial:
    spread_vertical(G, initial, row+1, col, rows, cols, start, end)




#main program
test_cases = int(raw_input())

for i in range(test_cases):
  test = raw_input()
  r_c = test.split()
  rows = int(r_c[0])
  cols = int(r_c[1])
  grid = []

  for r in range(rows):
    row = list(raw_input())
    grid.append(row)
  
  cake(grid, rows, cols)
  
  print "Case #{0}:".format(i + 1)

  for r in range(rows):
    print "".join(grid[r])