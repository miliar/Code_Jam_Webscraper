import sys

fin = sys.stdin

T = int(fin.readline())

for t in xrange(T):
  N, K = map(int, fin.readline().split())
  R = 2 ** N - 1
  if (K & R == R):
    print "Case #" + str(t+1) + ": ON"
  else:
    print "Case #" + str(t+1) + ": OFF"
   