#!/usr/bin/env python

import sys
from itertools import repeat

def parse(f):
  N, M = map(int, f.readline().split(' '))
  existing = []
  new = []
  for i in range(N):
    s = f.readline().strip()
    existing.append(s[1:].split('/'))
  for i in range(M):
    s = f.readline().strip()
    new.append(s[1:].split('/'))
  return (existing, new)

def addDir(tree, dir):
  c = 0
  if not dir in tree:
    tree[dir] = dict()
    c = 1
  return (c, tree[dir])

def addPath(tree, path):
  def f(a, dir):
    ac, tree = a
    c, subTree = addDir(tree, dir)
    return (c+ac, subTree)
  return reduce(f, path, (0, tree))

def solve(o):
  existing, new = o
  tree = dict()
  for path in existing:
    addPath(tree, path)

  sum = 0
  for path in new:
    c, tree1 = addPath(tree, path)
    # print path, c
    sum += c

  return sum

def main():
  f = sys.stdin
  n = int(f.readline())
  for i in range(n):
    o = parse(f)
    print 'Case #%d: %d' % (i+1, solve(o))

if __name__ == '__main__':
  main()
