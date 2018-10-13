#!/usr/bin/env python
import math, sys
from random import random

def sqr(x):
  return x*x
sqrt = math.sqrt

def solve(t):
  N, W, H = map(int, input.readline().split())
  R = map(int, input.readline().split())
  i = 0
  xs = [None for _ in xrange(N)]
  ys = [None for _ in xrange(N)]
  def dist2(i, j):
    return sqr(xs[i] - xs[j]) + sqr(ys[i] - ys[j])
  def min_dist2(i, j):
    return sqr(R[i] + R[j])
  def check(i):
    for j in xrange(i):
      if dist2(i, j) < min_dist2(i, j) - 1:
        return False
    return True

  while i < N:
    r = R[i]
    while True:
      xs[i] = round(random() * W)
      ys[i] = round(random() * H)
      if check(i):
        break
    i += 1

  def validate():
    for i in xrange(N):
      for j in xrange(i):
        d = sqrt(sqr(xs[i] - xs[j]) + sqr(ys[i] - ys[j]))
        if d < R[i] + R[j]:
          return False
    return True

  print validate()
  print >>output, 'Case #%d:' % t,
  for i in xrange(N):
    print >>output, xs[i], ys[i],
  print >>output


test = 'B-small-attempt1'

input = open('%s.in'%test)
output = open('%s.out'%test, 'w')
#output = sys.stdout

for t in xrange(1, int(input.readline())+1):
  solve(t)
