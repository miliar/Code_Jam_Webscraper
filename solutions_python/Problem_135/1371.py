#!/usr/bin/python

import sys

T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)
  # toks = sys.stdin.readline().strip().split()
  # A = int(toks[0])

  Arowi = int(sys.stdin.readline())
  A = []
  for i in range(4):
    toks = sys.stdin.readline().strip().split()
    A.append([int(t) for t in toks])

  Browi = int(sys.stdin.readline())
  B = []
  for i in range(4):
    toks = sys.stdin.readline().strip().split()
    B.append([int(t) for t in toks])

  Arow = A[Arowi-1]
  Brow = B[Browi-1]
  # print Arow,Brow

  intersect = []
  for n in Arow:
    if n in Brow:
      intersect.append(n)
  # print intersect

  ans = ""
  if len(intersect)==1:
    ans = str(intersect[0])
  elif len(intersect)==0:
    ans = "Volunteer cheated!"
  else:
    ans = "Bad magician!"
  print "Case #%d: %s" % (test+1, ans)

