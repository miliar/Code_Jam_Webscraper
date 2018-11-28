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

def is_palindrome(n):
  digits = list(str(n))
  reverse = digits[:]
  reverse.reverse()
  return digits == reverse

import math

io = IO("qual-c-small")
for case in xrange(io.read_number()):
  a, b = io.read_numbers()
  root_lower = int(math.floor(math.sqrt(a)))
  root_upper = int(math.ceil(math.sqrt(b))) + 1
  count = 0
  for root in xrange(root_lower, root_upper):
    square = root * root
    if square < a: continue
    if square > b: break
    if not is_palindrome(root): continue
    if not is_palindrome(square): continue
    count += 1
  io.write(count)
io.close()