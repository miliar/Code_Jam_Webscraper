
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  r, c = [int(x) for x in raw_input().split(' ')]

  grid = []
  for x in xrange(r):
      grid.append(list(raw_input()))

  new_grid = []
  for row_index, row in enumerate(grid):
      new_grid.append([])
      for column_index, column in enumerate(row):
          if column != '?':
              new_grid[row_index].append(column)
          elif column == '?':
              new_char = '?'
              for char in reversed(new_grid[row_index]):
                  if char != '?':
                      new_char = char
                      break
              else:
                  for char in row[column_index:]:
                      if char != '?':
                          new_char = char
                          break

              new_grid[row_index].append(new_char)


  for row_index, row in enumerate(new_grid):
    for column_index, column in enumerate(row):
        if column == '?':
            for index in xrange(row_index, -1, -1):
                if new_grid[index][column_index] != '?':
                    new_grid[row_index][column_index] = new_grid[index][column_index]
                    break
            else:
                for index in xrange(row_index, r):
                    if new_grid[index][column_index] != '?':
                        new_grid[row_index][column_index] = new_grid[index][column_index]
                        break


  print "Case #{}:".format(i)
  for row in new_grid:
    print "".join(row)
  # check out .format's specification for more formatting options
