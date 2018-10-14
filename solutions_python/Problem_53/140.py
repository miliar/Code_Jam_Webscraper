import sys

def getint():
  return int(sys.stdin.readline())

def getints():
  return [int(s) for s in sys.stdin.readline().split()]

def solve(N, K):
  if K % 2**N == (2**N-1):
    return 'ON'
  return 'OFF'

T = getint()
for i in range(T):
  N, K = getints()
  print 'Case #%d: %s' % (i+1, solve(N, K))