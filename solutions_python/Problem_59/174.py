#! /usr/bin/python

import sys

class TreeNode:
  def __init__(self, dir):
    self.dir = dir
    self.next = []

  def dir_present(self, dir):
    for i in self.next:
      if dir == i.dir:
        return i
    return None

def solve(existing, to_create):
#  print existing
#  print to_create

  arbo = TreeNode("")

  for p in existing:
    ptr_arbo = arbo
    for d in p:
      nxt = ptr_arbo.dir_present(d)
      if nxt == None:
        ptr_arbo.next.append(TreeNode(d))
        nxt = ptr_arbo.dir_present(d)

      ptr_arbo = nxt

  num_mkdir = 0

  for p in to_create:
    ptr_arbo = arbo
    for d in p:
      nxt = ptr_arbo.dir_present(d)
      if nxt == None:
#        print p, d
        num_mkdir += 1
        ptr_arbo.next.append(TreeNode(d))
        nxt = ptr_arbo.dir_present(d)

      ptr_arbo = nxt

  return num_mkdir


fd = open(sys.argv[1])
num_cases = int(fd.readline())

for j in range(0, num_cases):
  (n, m) = [int(item) for item in fd.readline().split(" ")]
  existing = [[""]]
  for i in xrange(n):
    path = fd.readline().split("\n")[0]
    existing.append(path.split("/"))

  to_create = []
  for i in xrange(m):
    path = fd.readline().split("\n")[0]
    to_create.append(path.split("/"))

  output = solve(existing, to_create)
  print "Case #%d:" % (j+1), output

