#!/usr/bin/env python
'''
Google Code Jam 2008
Problem: 
@euphoria
'''
import sys

def combinations(items, n):
  if n==0: yield []
  else:
    for i in xrange(len(items)):
      for cc in combinations(items[i+1:],n-1):
        yield [items[i]]+cc

def trees(n, X, Y, A, B, C, D, M):
  out = [(X,Y)]
  for i in xrange(1,n):
    X = (A * X + B) % M
    Y = (C * Y + D) % M
    out.append((X,Y))
  return out

def center((x1, y1), (x2, y2), (x3, y3)):
  return ((x1 + x2 + x3)/3.0,(y1+y2+y3)/3.0)

def isint(f):
  from math import floor
  return floor(f) == f

def main(argv=None):
  if argv is None:
    argv = sys.argv

  f = file("A-small-attempt0.in")
  cases = int(f.readline())
  for case in xrange(1,cases+1):
    n, A, B, C, D, x0, y0, M = f.readline().split()
    n = int(n); A = int(A); B = int(B); C = int(C); D = int(D)
    x0 = int(x0); y0 = int(y0); M = int(M)
    
    winners = 0
 
    t = trees(n, x0, y0, A, B, C, D, M)
    for c in combinations(t,3):
      cc = center(c[0], c[1], c[2])
      if isint(cc[0]) and isint(cc[1]):
        winners = winners + 1

    print 'Case #%s: %s' % (case,winners)

if __name__ == '__main__':
  sys.exit(main())
