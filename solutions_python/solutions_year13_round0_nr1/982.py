#!/usr/bin/env python

import sys

def rl():
  return sys.stdin.readline().strip()

def solve_one():
  def tr(c, T):
    c = T if c == 'T' else c
    if c == 'X':
      return 1
    elif c == 'O':
      return -1
    else:
      return 0

  data = [rl() for i in xrange(4)]
  rl()
  for T in ['X','O']:
    count = [0] * 10
    for i in xrange(4):
      for j in xrange(4):
        count[i] += tr(data[i][j], T)
        count[4+i] += tr(data[j][i], T)
      count[8] += tr(data[i][i], T)
      count[9] += tr(data[i][3-i], T)
    for c in count:
      if c == 4:
        return 'X won'
      elif c == -4:
        return 'O won'
  return 'Game has not completed' if '.' in ''.join(data) else 'Draw'

def main():
  for i in xrange(int(rl())):
    print 'Case #%d: %s' % (i+1,solve_one())

if __name__ == '__main__':
  main()
