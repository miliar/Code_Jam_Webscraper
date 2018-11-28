import sys

f = open(sys.argv[1], 'r')

T = int(f.readline())

def isgood(x, numbers):
  for n in numbers:
    if x > n:
      if x % n != 0:
        return False
    elif x < n:
      if n % x != 0:
        return False
  return True

for t in xrange(T):
  N, L, H = [int(x) for x in f.readline().strip().split(' ')]
  numbers = [int(x) for x in f.readline().strip().split(' ')]
  
  possible = range(L, H + 1)
  for n in numbers:
    possible = filter(lambda x: isgood(x, numbers), possible)
  
  print 'Case #%d:' % (t + 1), 'NO' if len(possible) == 0 else str(min(possible))

f.close()
