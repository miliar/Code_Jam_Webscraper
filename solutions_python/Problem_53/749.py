


def go(N, K):
  while N:
    N -= 1;
    if not (K & (1<<N)):
      return 'OFF'
  return 'ON'
  

T = int(raw_input())
for t in xrange(T):
  print 'Case #%d: %s' % (t+1, go(*map(int,raw_input().split())))