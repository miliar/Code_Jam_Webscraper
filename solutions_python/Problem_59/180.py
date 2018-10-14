#!/usr/bin/python
from sys import stdin

def add_path(p, dirs):
  added = 0
  path = dirs
  components = p.split('/')[1:]
  
  while components:
    h = components.pop(0)
    if not (h in path):
      path[h] = {}
      added += 1
    path = path[h]
  
  return added

def read_paths(n, dirs):
  added = 0
  for _ in xrange(n):
    added += add_path(stdin.readline().strip(), dirs)
  return added

cases = int(stdin.readline())

for _ in xrange(cases):
  dirs = {}
  args = stdin.readline()
  existing, new = map(int, args.split(' '))
  read_paths(existing, dirs)
  added = read_paths(new, dirs)
  print "Case #" + str(_ + 1) + ": " + str(added)
