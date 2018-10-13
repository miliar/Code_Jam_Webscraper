from sys import stdin

trials  = int(stdin.readline())

for case in xrange(trials):
  pairs = int(stdin.readline())
  A = []
  B = []
  for pair in xrange(pairs):
    a,b = map(int, stdin.readline().split())
    A.append(a)
    B.append(b)
  crosses = sum(1 for i, an in enumerate(A) for j, ak in enumerate(A[i:]) if (an < ak and B[i] > B[i+j]) or (an > ak and B[i] < B[i+j]))
  print "Case #%d: %d" % (case + 1, crosses)