#! /usr/bin/python

fd = open("input.in")

num_cases = int(fd.readline())

for i in range(0, num_cases):
  (n, A, B, C, D, x0, y0, M) = fd.readline().split(" ")
  n = int(n)
  A = int(A)
  B = int(B)
  C = int(C)
  D = int(D)
  x0 = int(x0)
  y0 = int(y0)
  M = int(M)

  trees = []
  trees.append((x0, y0))
  X = x0
  Y = y0
  for t in range(1, n):
    X = (A * X + B) % M
    Y = (C * Y + D) % M
    trees.append((float(X), float(Y)))

  num_triangle = 0

  for t1 in range(0,n):
    for t2 in range(0,t1):
      for t3 in range(0,t2):
        xmoy = (trees[t1][0] + trees[t2][0] + trees[t3][0])/3
        ymoy = (trees[t1][1] + trees[t2][1] + trees[t3][1])/3
        if xmoy == int(xmoy) and ymoy == int(ymoy):
          num_triangle += 1
        
  print "Case #%d:" % (i+1), num_triangle
