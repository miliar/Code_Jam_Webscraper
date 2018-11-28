import operator as op
from functools import reduce

for case in range(1, int(input()) + 1):
  N = int(input())
  candy = sorted(int(i) for i in input().split())

  r = 'NO'
  if not reduce(op.xor, candy, 0):
    r = sum(candy[1:])

  print('Case #%d: %s' % (case, r))
