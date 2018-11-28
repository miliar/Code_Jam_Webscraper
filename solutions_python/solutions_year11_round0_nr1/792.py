#from math import abs
from sys import stdin
from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def trial(moves):
  cost = 0
  position = {'O': 1, 'B': 1}
  last_robot = None
  last_cost = 0

  for (robot, next_location) in moves:
    loc = int(next_location)
    next_cost = abs(position[robot] - loc) + 1
    if robot != last_robot:
      next_cost = max(1, next_cost - last_cost)
      last_robot = robot
      last_cost = next_cost
    else:
      last_cost += next_cost
    position[robot] = loc
    cost += next_cost
  return cost

with open('C:\Users\Erin\Downloads\A-large.in') as f:
  n = int(f.readline())
  with open('A-large.out', 'w+') as out:
    for i in xrange(1, n+1):
      line = f.readline()
      moves = grouper(2, line.split()[1:])
      cost = trial(moves)
      print >> out,  'Case #%d: %d' % (i, cost)