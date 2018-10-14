if __name__ == '__main__':
  #f = open('test.txt')
  f = open('Downloads/C-small-attempt0.in') 
  case = int(f.readline())
  for i in range(1,case+1):
    cost = 0
    r, k, n = [ int(x) for x in f.readline().strip().split() ]
    queue = [ int(x) for x in f.readline().strip().split() ]
    for j in xrange(r):
      s = 0
      for m in range(n):
        if s + queue[m] > k:
          break
        s += queue[m]
      cost += s
      on_coaster = [queue[x] for x in range(m)]
      for x in on_coaster:
        queue.remove(x)
      queue.extend(on_coaster)
    print 'Case #%d: %d'%(i,cost) 
