#! /usr/bin/python -tt

import sys

def ReadInts(f):
  return list(map(int, f.readline().strip().split(" ")))

def ReadPath(f):
  return f.readline().strip().split("/")

counter = 0
enabled = False

class ppath:
  def __init__(self, n):
    self.name = n
    self.child = []
  def add(self, path):
    global counter
    if len(path) == 0:
      return
    found = False
    for p in self.child:
      if p.name == path[0]:
        if len(path) > 1:
          p.add(path[1:])
        found = True
        break
    if not found:
      counter += 1
      a = ppath(path[0])
      if enabled:
        print path[0]
      if len(path) > 1:
        a.add(path[1:])
      self.child.append(a)

f = open(sys.argv[1], 'r')
t = ReadInts(f)[0]
for i in range(1, t+1):
  (n, m) = ReadInts(f)
  root = ppath("")
  create = 0
  for x in xrange(1, n+1):
    root.add(ReadPath(f)[1:])
#    print ReadPath(f)
  counter = 0
#  enabled = True
  for x in xrange(1, m+1):
    root.add(ReadPath(f)[1:])
#    print ReadPath(f)
#  for a in root.child.child:
#    print a.name

  print "Case #%d: %s" % (i, counter)
  del root


