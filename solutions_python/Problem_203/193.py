file_in = open('A-large.in', 'r')
file_out = open('a.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  r, c = map(int, file_in.readline().split())
  grid = []
  for i in range(r):
    grid.append(list(file_in.readline().strip()))

  for row in grid:
    # find the first non-empty character in the row
    for space in row:
      if space != '?':
        char = space
        break
    else:
      continue
    for i in range(c):
      if row[i] != '?':
        char = row[i]
      row[i] = char
  
  copy = ""
  for row in grid:
    if row[0] != "?":
      copy = row
      break
  for i in range(r):
    if(grid[i][0] != "?"):
      copy = grid[i]
    grid[i] = copy



  file_out.write("Case #{}:\n".format(t))
  file_out.write("\n".join("".join(row) for row in grid))
  file_out.write('\n')