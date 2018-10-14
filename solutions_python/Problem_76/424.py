import sys
import math

input = sys.stdin
N = int(input.readline())
for n in xrange(1, N+1):
  i = int(input.readline())
  data = map(int, input.readline().split(' '))

  value_max = 0
  data.sort()

  for j in xrange(1, len(data)):
    left = data[:j]
    right = data[j:]
    r_left = reduce(lambda c,d: c^d, left)
    r_right = reduce(lambda c,d: c^d, right)

    if r_left == r_right and r_left > 0:
      value_max = max(value_max, max(sum(left), sum(right)))

  print 'Case #%d: %s'%(n, value_max if value_max > 0 else 'NO')
      
