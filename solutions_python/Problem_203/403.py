# AXIS_X = "x"
# AXIS_Y = "y"
# DIR_FD = "forward" # right or down
# DIR_BK = "backward" # up or left

# def pull_axis(grid, x, y, axis, dirc):
#   nrows, ncols = len(grid), len(grid[0])
#   sweep_width = {AXIS_X: nrows, AXIS_Y: ncols}[axis]
#   sweep_len   = {AXIS_X: ncols, AXIS_Y: nrows}[axis]
#   acc = ["?"] * sweep_width
#   for i in xrange(swee):

def pradoop(acc, row):
  """Merge with forcely ra"""
  s = []
  for a, b in zip(acc, row):
    if b != "?":
      s += [b]
    else:
      s += [a]
  return s

assert pradoop(list("???"), list("abc")) == list("abc")
assert pradoop(list("?d?"), list("abc")) == list("abc")
assert pradoop(list("???"), list("???")) == list("???")
assert pradoop(list("abc"), list("???")) == list("abc")
assert pradoop(list("abc"), list("?X?")) == list("aXc")

def pull_down(grid):
  nrows, ncols = len(grid), len(grid[0])
  acc = ["?"] * ncols
  newgrid = []
  for i in xrange(nrows):
    acc = pradoop(acc, grid[i])
    newgrid.append(acc)
  return newgrid

def flip_vert(grid):
  return grid[::-1]

def flip_hor(grid):
  return [row[::-1] for row in grid]

def rotate(grid):
  # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
  return zip(*grid[::-1])

def solve(grid):
  g = grid
  g = pull_down(g)
  g = flip_vert(g)
  g = pull_down(g)
  g = flip_vert(g)
  g = rotate(g)
  g = pull_down(g)
  g = flip_vert(g)
  g = pull_down(g)
  g = flip_vert(g)
  g = rotate(g)
  g = rotate(g)
  g = rotate(g)
  return g

def print_grid(grid):
  for row in grid:
    print "".join(row)

if __name__ == "__main__":
  n_tests = int(raw_input())
  for i in xrange(n_tests):
    nrows, ncols = map(int, raw_input().split(" "))
    grid = []
    for y in xrange(nrows):
      letters = list(raw_input())
      grid.append(letters)
    solved = solve(grid)
    print "Case #{}:".format(i+1)
    print_grid(solved)
