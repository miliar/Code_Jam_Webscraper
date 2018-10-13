#!/usr/bin/python -O

import sys

def solve(c,f,x):
  cost = 0.0
  rate = 2.0
  while True:
    z = x/rate
    u = c/rate
    v = x/(rate+f)
    if z > (u + v):
      cost += u
      rate += f
    else:
      break
  return cost + z

def main(argv=None):
  if argv is None:
    argv = sys.argv
  g = open(sys.argv[1], 'r')
  n = int(g.readline())
  n_case = 1
  while n_case <= n:
    values = g.readline().split()
    c,f,x= [float(x) for x in values]
    cost = solve(c,f,x)
    print "Case #" + str(n_case) + ': ' + "%0.7f" % cost
    n_case += 1
  g.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
