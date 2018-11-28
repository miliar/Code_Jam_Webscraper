import sys

def check_complete(d_lawn, lawn, rows, cols):
  for row in xrange(rows):
    for col in xrange(cols):
      if lawn[row][col] != d_lawn[row][col]:
        return False
  return True

def check_row_mowable(d_lawn, row, cols):
  h = d_lawn[row][0]
  for col in xrange(cols):
    if h < d_lawn[row][col]:
      return False
  return True
  

def check_col_mowable(d_lawn, col, rows):
  h = d_lawn[0][col]
  for row in xrange(rows):
    if h < d_lawn[row][col]:
      return False
  return True
  

def mow_row(d_lawn, lawn, row, cols):
  h = max(d_lawn[row])
  for col in xrange(cols):
    lawn[row][col] = min(h, lawn[row][col])


def mow_col(d_lawn, lawn, col, rows):
  h = max([x[col] for x in d_lawn])
  for row in xrange(rows):
    lawn[row][col] = min(h, lawn[row][col])

def check_col_oppo_mowable(d_lawn, col, rows):
  h = d_lawn[rows-1][col]
  for row in xrange(rows):
    if h < d_lawn[row][col]:
      return False
  return True


def check_row_oppo_mowable(d_lawn, row, cols):
  h = d_lawn[row][cols-1]
  for col in xrange(cols):
    if h < d_lawn[row][col]:
      return False
  return True

def mow_col_oppo(d_lawn, lawn, col, rows):
  h = d_lawn[rows-1][col]
  for row in xrange(rows):
    lawn[row][col] = min(h, lawn[row][col])

def mow_row_oppo(d_lawn, lawn, row, cols):
  h = d_lawn[row][cols - 1]
  for col in xrange(cols):
    lawn[row][col] = min(h, lawn[row][col])


def mow_inner_cells(d_lawn, lawn, rows, cols):
  result = True
  if rows > 2:
    for row in range(1, rows-1):
      if check_row_mowable(d_lawn, row, cols):
        mow_row(d_lawn, lawn, row, cols)
#        return False
  if cols > 2:
    for col in range(1, cols - 1):
      if check_col_mowable(d_lawn, col, rows):
        mow_col(d_lawn, lawn, col, rows)
#        return False
  return True
        

def mow(d_lawn, lawn, rows, cols):
  for row in xrange(rows):
        mow_row(d_lawn, lawn, row, cols)
  for col in xrange(cols):
        mow_col(d_lawn, lawn, col, rows)
  return True

def process_corners(d_lawn, lawn, rows, cols):
  if check_col_mowable(d_lawn, 0, rows) and check_col_mowable(d_lawn, cols-1, rows):
    mow_col(d_lawn, lawn, 0, rows)
    mow_col(d_lawn, lawn, cols-1, rows)
  if check_row_mowable(d_lawn,  0, cols) and check_row_mowable(d_lawn, rows-1, cols):
    mow_row(d_lawn, lawn, 0, cols)
    mow_row(d_lawn, lawn, rows-1, cols)
  return True


def lawn_mower(d_lawn, rows, cols):
  lawn = []
  for row in xrange(rows):
    lawn.append([100] * cols)
  if rows == 1 or cols == 1:
    return "YES"
  mow(d_lawn, lawn, rows, cols)
  if check_complete(d_lawn, lawn, rows, cols):
    return "YES"
  else:
    return "NO"

readline = sys.stdin.readline
total = int(sys.stdin.readline())
for m in xrange(total):
  dim = readline().split()
  rows = int(dim[0])
  cols = int(dim[1])
  lawn = []
  for r in xrange(rows):
    lawn.append([int(x)  for x in readline().split()])
  result = lawn_mower(lawn, rows,cols)
  print "Case #%d: " % (m+1) + result
#  for row in xrange(rows):
#    print lawn[row]



