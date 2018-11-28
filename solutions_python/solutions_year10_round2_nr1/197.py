import sys

input = open(sys.argv[1])
n = int(input.readline())

for nCase in xrange(1, n+1):
  M, N= map(lambda x: int(x), input.readline().strip().split(' ') )
  
  d = []
  for i in xrange(M):
    d.append(input.readline().strip())
  

  res = 0

  for i in xrange(N):
    a = input.readline().strip().split('/')
   
    path = []
    p = ''
    for j in xrange(1, len(a)):
      p += '/' + a[j]

      if not p in d:
        d.append(p)
        res+=1

  print 'Case #%d: %s'%(nCase, res)
