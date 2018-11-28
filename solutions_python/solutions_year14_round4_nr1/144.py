from sys import argv
from copy import copy

def read_input(f):
  lines = open(f, 'r')
  T = int(lines.readline().strip())


  for i in xrange(T):
    N, disk_cap = map(int, lines.readline().strip().split(' '))
    
    files = sorted(map(int, lines.readline().strip().split(" ")))

    yield i+1, N, disk_cap, files

  lines.close()

def knapsack(N, disk_cap, files):
  i = N - 1
  counter = 0
  while i >= 0:
    d1 = files.pop()
    D = [d for d in files if d <= disk_cap - d1]
    if len(D) > 0:
      d2 = max(D)
      files.remove(d2)
      i -= 2
    else:
      i -= 1
    counter += 1

  return counter

if __name__ == '__main__':
  for test_case, N, disk_cap, files in read_input(argv[1]):
    #print " - - - "
    
    res = knapsack(N, disk_cap, files)     
    print "Case #%d: %s" % (test_case, res)

