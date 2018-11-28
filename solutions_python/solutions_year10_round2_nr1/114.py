











T = int(raw_input())
for t in xrange(T):
  N, M = map(int,raw_input().split())
  D = [raw_input() for n in xrange(N)]
  E = [raw_input() for m in xrange(M)]
  
  dirs = {}
  for d in D:
    path = d.split('/')
    for i in xrange(1,len(path)):
      p = '/'.join(path[0:i+1])
      # print '1:',p
      dirs[p] = 1
      
  c = 0
  for d in E:
    path = d.split('/')
    for i in xrange(1,len(path)):
      p = '/'.join(path[0:i+1])
      # print '2:',p
      if p not in dirs:
        c += 1
        dirs[p] = 1
        
  print 'Case #%d: %d' % (t+1, c)
