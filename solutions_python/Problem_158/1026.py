#!/usr/bin/python

import fileinput

def solve(x, r, c):
  if x >= 7 and r >= 3 and c >= 3:
    return 'RICHARD'
  if x == 1:
    return 'GABRIEL'
  if (r * c) % x == 0 :
    if x == 2:
      return 'GABRIEL'
    if x in [3,4,5,6] and r >= x - 1 and c >= r - 1:
      return 'GABRIEL'

  return 'RICHARD'
    

if __name__ == '__main__':
  fin = fileinput.input()
  t = int(fin.readline())
  for i in range(t):
    out = None
    x, r, c = [int(_i) for _i in fin.readline().strip().split()]
    out = solve(x ,r ,c)
    print 'Case #{0}: {1}'.format(i + 1, out)
