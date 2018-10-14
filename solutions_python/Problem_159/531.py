from sys import argv
from copy import copy

def read_input(f):
  lines = open(f, 'r')
  T = int(lines.readline().strip())

  for i in xrange(T):
    _ = lines.readline()
    mushrooms = map(int, lines.readline().strip().split(' '))

    yield i+1, mushrooms
  lines.close()

def min_mushrooms(mushrooms):
  n = len(mushrooms)
  count_method1 = 0
  delta_method2 = 0
  for i in xrange(n-1):
    if mushrooms[i] > mushrooms[i+1]:
      delta = mushrooms[i] - mushrooms[i+1]
      count_method1 += delta
      if delta > delta_method2:
        delta_method2 = delta

  count_method2 = 0
  for i in xrange(n-1):
    diff = min(mushrooms[i], delta_method2)
    count_method2 += diff

  return count_method1, count_method2

if __name__ == '__main__':
  for test_case, digits in read_input(argv[1]):
    c1, c2 = min_mushrooms(digits)     
    print "Case #%d: %d %d" % (test_case, c1, c2)
