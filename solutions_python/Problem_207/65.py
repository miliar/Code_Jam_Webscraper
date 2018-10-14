import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, R, O, Y, G, B, V ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  res = 0
  m = max(R, Y, B)
  if m > N/2: res = "IMPOSSIBLE"
  else:
    res = ''
    if R > 0:
      res += 'R'
      R -= 1
    elif B > 0:
      res += 'B'
      B -= 1
    elif Y > 0:
      res += 'Y'
      Y -= 1
    else: assert(False)
    for n in xrange(N-1):
      if res[-1] == 'R':
        if B >= Y:
          res += 'B'
          B -= 1
        else:
          res += 'Y'
          Y -= 1
      elif res[-1] == 'B':
        if R >= Y:
          res += 'R'
          R -= 1
        else:
          res += 'Y'
          Y -= 1
      elif res[-1] == 'Y':
        if R >= B:
          res += 'R'
          R -= 1
        else:
          res += 'B'
          B -= 1
      else: assert(False)
  print "Case #%d: %s" % (1+tmp_tc, res)

