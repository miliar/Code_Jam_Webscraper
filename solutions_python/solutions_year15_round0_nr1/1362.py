from sys import argv
from copy import copy

def read_input(f):
  lines = open(f, 'r')
  T = int(lines.readline().strip())

  for i in xrange(T):
    _, digits = lines.readline().strip().split(' ')

    yield i+1, len(digits), digits
  lines.close()

def count_guests(T, digits):
  counter = 0
  result = 0
  for i in xrange(T):
    d = int(digits[i])
    delta = 0
    if d > 0:
      if i > counter:
        delta = i - counter
        
        if delta > 0:
          result+= delta
          counter += delta
      counter += d

  return result
if __name__ == '__main__':
  for test_case, N, digits in read_input(argv[1]):
    res = count_guests(N, digits)     
    print "Case #%d: %s" % (test_case, res)
