import sys

def getAttempts(C, W):
  newC = C - W
  if C == W:
    return W
  elif C < 2*W:
    return W + 1
  else:
    return 1 + getAttempts(newC, W)

T = int(sys.stdin.readline())
for case in range(1, T + 1):
  R, C, W = [int(i) for i in sys.stdin.readline().split()]
  result = getAttempts(C, W)
  print "Case #%s: %s" %(case, result)