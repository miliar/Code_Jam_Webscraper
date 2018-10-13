#!/usr/bin/python

import sys

def pop_smallest_above(L,x,d=0):
  ind = d
  for i in range(len(L)):
    v = L[i]
    if v > x:
      ind = i
      break
  return L.pop(ind)


T = int(sys.stdin.readline())
for test in range(T):
  print >> sys.stderr, "Test: %d" % (test+1)

  N = int(sys.stdin.readline())

  # Naomi's blocks
  A = sys.stdin.readline().strip().split()
  A.sort()

  # Ken's blocks
  B = sys.stdin.readline().strip().split()
  B.sort()

  # keep A and B as strings for precision

  # print A,B

  W = 0
  Aw = list(A)
  Bw = list(B)
  for i in range(N):
    x = Aw.pop()
    y = pop_smallest_above(Bw,x)
    # print x,y
    if x > y:
      W += 1

  D = 0
  Ad = list(A)
  Bd = list(B)
  for i in range(N):
    # Al = A[0]
    # Ah = A[-1]
    # Bl = B[0]
    # Bh = B[-1]

    # # select smallest block and force Ken to select largest
    # x = Ad.pop(0)
    # y = Bd.pop()

    # force Ken to select smallest, and only just beat him, if possible
    y = Bd.pop(0)
    x = pop_smallest_above(Ad,y)

    # print x,y
    if x > y:
      D += 1

  print "Case #%d: %d %d" % (test+1, D, W)

