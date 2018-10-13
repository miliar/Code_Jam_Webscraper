f = open('b.in', 'r')
T = int(f.readline())
for t_no in range(T):
  p = int(f.readline())
  M = [int(x) for x in f.readline().split()]
  P = [[100000 * (2 ** 13)] * (p + 1) for x in range(2 ** p)]
  for i in range(len(P)):
    for j in range(M[i] + 1):
      P[i][j] = 0
  for i in range(p):
    ct = [int(x) for x in f.readline().split()]
    A = [[0] * (p + 1) for x in range(len(ct))]
    for i in range(len(ct)):
      for j in range(p + 1):
        A[i][j] = P[2 * i][j] + P[2 * i + 1][j] + ct[i]
        if j:
          A[i][j - 1] = min(A[i][j-1], P[2 * i][j] + P[2 * i + 1][j])
      for j in range(p - 1, -1, -1):
        A[i][j] = min(A[i][j], A[i][j + 1])
    P = A
  sol = P[0][0]
  print 'Case #%s: %s' % (t_no + 1, sol)
