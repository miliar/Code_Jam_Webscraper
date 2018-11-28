import sys

input = open(sys.argv[1])
n = int(input.readline())

for nCase in xrange(1, n+1):
  N = int(input.readline().strip())

  a = []
  b = []
  for i in xrange(N):
   ai, bi = map(lambda x: int(x), input.readline().strip().split(' ') )
   a.append(ai)
   b.append(bi)


  res = 0
  for i in xrange(N):
    for j in xrange(i+1, N):

      if (a[i] - a[j] >= 0 and b[i] - b[j] <= 0) or (a[i] - a[j] <= 0 and b[i] - b[j] >= 0):
        res += 1

  print 'Case #%d: %s'%(nCase, res)
