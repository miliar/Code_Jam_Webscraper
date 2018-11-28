problem = "C"
inf = open("../data/" + problem + ".in", "r")
outputs = []
outf = open("../data/" + problem + ".out", "w")
datasets = int(inf.readline())
for dataset in range(datasets):
  rcm = inf.readline().strip().split(" ")
  rows = int(rcm[0])
  cols = int(rcm[1])
  mines = int(rcm[2])
  blanks = rows * cols - mines
  result = []
  if rows == 1:
    result = ["c" + "".join(["."] * (cols - mines - 1)) + "".join(["*"] * mines)]
  elif cols == 1:
    result = ["c"] + ["."] * (rows - mines - 1) + ["*"] * mines
  elif blanks == 1:
    result = ["c" + "*" * (cols - 1)] + ["*" * cols] * (rows - 1)
  else:
    switched = (rows > cols)
    width = rows if switched else cols
    height = rows * cols / width
    grid = [width] * (blanks / width) + [blanks % width] + [0] * (rows - blanks / width - 1)
    if blanks / width < 2 and blanks > 2 and blanks % 2 == 0:
      grid = [blanks / 2, blanks / 2] + [0] * (height - 2)
    elif blanks / width < 2 and blanks > 8 and height > 2:
      grid = [blanks / 2 - 1, blanks / 2 - 1, 3] + [0] * (height - 3)
    elif blanks / width == 2 and blanks > 8 and blanks % width == 1:
      grid = [width - 1, width - 1, 3] + [0] * (height - 3)
    elif blanks / width > 2 and blanks > 8 and blanks % width == 1:
      grid = [width] * (blanks / width - 1) + [width - 1, 2] + [0] * (height - 1 - blanks / width)
    elif blanks / width >= 2 and blanks % width != 1:
      grid = [width] * (blanks / width) + [blanks % width] + [0] * (rows - blanks / width - 1)
    else:
      result = ["Impossible"]
    if not result:
      for row in range(rows):
        if switched:
          this_row = []
          for col in range(cols):
            if grid[col] > row:
              this_row.append('.')
            else:
              this_row.append('*')
        else:
          this_row = ['.'] * grid[row] + ['*'] * (cols - grid[row])
        if row == 0:
          this_row[0] = 'c'
        result.append("".join(this_row))
    print str(dataset) + str(result)
        
  outputs.append("Case #" + str(dataset + 1) + ":\n" + "\n".join(result))
outf.write("\n".join(outputs))
print "\n".join(outputs)