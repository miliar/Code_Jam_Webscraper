#!/usr/bin/env python

import sys
from itertools import repeat

def parse(f):
  n, k = map(int, f.readline().split(' '))
  a = []
  for i in range(n):
    s = f.readline().strip()
    # a.append([ch for ch in s])
    a.append(s)
  return (n, k, a)

def rotate(N, m):
  return [''.join([m[N-c-1][r] for c in range(N)]) for r in range(N)]

def gravityL(N, m):
  for r in range(N):
    s = m[r]
    s = s.replace('.', '')
    s = ''.join(repeat('.', N-len(s))) + s
    m[r] = s
  return m

def check(N, K, m):
  rc = reduce(lambda a, j: a + [(i, j) for i in range(N)], range(N), [])
  red = False
  blue = False
  for r, c in rc:
    s = ''
    s += checkD(N, K, m, r, c)
    s += checkR(N, K, m, r, c)
    s += checkDR(N, K, m, r, c)
    s += checkDL(N, K, m, r, c)
    # print '  r=%d c=%d s=%s' % (r, c, s)
    blue = blue or -1 < s.find('B')
    red = red or -1 < s.find('R')
  if blue and red:
    return 'Both'
  elif blue:
    return 'Blue'
  elif red:
    return 'Red'
  else:
    return 'Neither'

def checkD(N, K, m, r, c):
  ch = m[r][c]
  if '.'==ch:
    return ''
  if N < c + K:
    return ''
  for c in range(c+1, c+K):
    if ch != m[r][c]:
      return ''
  return ch

def checkR(N, K, m, r, c):
  ch = m[r][c]
  if '.'==ch:
    return ''
  if N < r + K:
    return ''
  for r in range(r+1, r+K):
    if ch != m[r][c]:
      return ''
  return ch

def checkDR(N, K, m, r, c):
  ch = m[r][c]
  if '.'==ch:
    return ''
  if N < r + K or N < c + K:
    return ''
  for i in range(1, K):
    if ch != m[r+i][c+i]:
      return ''
  return ch

def checkDL(N, K, m, r, c):
  ch = m[r][c]
  if '.'==ch:
    return ''
  if N < r + K or c < K - 1:
    return ''
  for i in range(1, K):
    if ch != m[r+i][c-i]:
      return ''
  return ch

def solve(o):
  N, K, m = o
  # m = rotate(N, m)
  m = gravityL(N, m)
  return check(N, K, m)

def main():
  f = sys.stdin
  n = int(f.readline())
  for i in range(n):
    o = parse(f)
    print 'Case #%d: %s' % (i+1, solve(o))

if __name__ == '__main__':
  main()
