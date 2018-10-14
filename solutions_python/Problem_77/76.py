import sys

A = [[1], [0, 1]]
fct = [1, 1]
for i in xrange(2, 1001):
  B = [0] * (i + 1)
  for c in xrange(0, i):
    if c:
      B[c - 1] += A[-1][c] * c
    B[c] += A[-1][c] * (i - 1 - c)
    B[c + 1] += A[-1][c]
  A.append(B)
  fct.append(fct[-1] * i)

p = [0, 0]
for i in xrange(2, 1001):
  s = fct[i]
  for x in xrange(1, i + 1):
    s += p[i - x] * A[i][x]
  p.append(s / (fct[i] - A[i][0]))

# Apparently p[i] = i, i > 1

T = int(sys.stdin.readline())
for test in xrange(T):
  n = int(sys.stdin.readline())
  A = [int(x) for x in sys.stdin.readline().split()]
  B = sorted(A)
  res = p[sum(1 for i in xrange(len(A)) if A[i] != B[i])]
  print 'Case #%s: %.6f' % (test + 1, res)
