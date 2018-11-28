class IO (object):
  def __init__(self, tag):
    self._in = file("codejam-%s.in"%tag, 'r')
    self._out = file("codejam-%s.out"%tag, 'w')
    self._case = 0
  
  def close(self):
    self._in.close()
    self._out.close()

  def read_string(self):
    return self._in.readline()
  
  def read_number(self):
    return int(self._in.readline())
  
  def read_numbers(self):
    return [int(x) for x in self._in.readline().split()]

  def write(self, template, *args):
    solution = str(template)%args
    self._case += 1
    line = "Case #%i: %s\n"%(self._case, solution)
    self._out.write(line)    

def is_line_of(c, line):
  return all(t == 'T' or t == c for t in line)

def lines(grid):
  for row in grid:
    yield row
  for col in xrange(4):
    yield [grid[i][col] for i in xrange(4)]
  yield [grid[i][i] for i in xrange(4)]
  yield [grid[i][3-i] for i in xrange(4)]

def has_line_of(c, grid):
  return any(is_line_of(c, line) for line in lines(grid))

io = IO("qual-a-large")
for case in xrange(io.read_number()):
  grid = [io.read_string().strip() for x in xrange(4)]
  io.read_string()
  if has_line_of('X', grid):
    io.write("X won")
  elif has_line_of('O', grid):
    io.write("O won")
  elif not any('.' in line for line in grid):
    io.write("Draw")
  else:
    io.write("Game has not completed")
io.close()