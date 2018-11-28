#!/usr/bin/env python

def solve(R, C, rows):
  for i in range(0, R):
    for j in range(0, C):
      if rows[i][j] == '#' and j+1<C and rows[i][j+1] == '#' and i+1<R and rows[i+1][j] == '#' and rows[i+1][j+1] == '#':
        rows[i][j] = '/'
        rows[i+1][j] = "\\"
        rows[i][j+1] = "\\"
        rows[i+1][j+1] = '/'
      elif rows[i][j] == '#':
        return 'Impossible'
  return "\n".join([''.join(r) for r in rows])

if __name__ == "__main__":
  import sys
  T = int(sys.stdin.readline())
  for t in range(1, T+1):
    R,C = map(int, sys.stdin.readline().split())
    rows = [list(sys.stdin.readline().replace("\n","")) for r in range(0,R)]
    print 'Case #{0}:'.format(t)
    print solve(R, C, rows)

