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

def sort_squares(rows, cols, lawn):
  res = []
  for r in xrange(rows):
    for c in xrange(cols):
      res.append((lawn[r][c], r, c))
  res.sort()
  return res

def check(rows, cols, lawn_rows):
  lawn_columns = zip(*lawn_rows);
  squares = sort_squares(rows, cols, lawn_rows)
  for value, r, c in squares:
    if all(v <= value for v in lawn_rows[r]):
      continue
    if all(v <= value for v in lawn_columns[c]):
      continue
    return False
  return True
  
def read_lawn(io):
  r, c = io.read_numbers()
  return r, c, [io.read_numbers() for x in xrange(r)]    

io = IO("qual-b-large")
for case in xrange(io.read_number()):
  if check(*read_lawn(io)):
    io.write("YES")
  else:
    io.write("NO")
io.close()