import sys

def print_dset(d, N, M):
  for i in range(N):
    for j in range(M):
      print d[i][j],
    print

def new_dset(N=100, M=100, h=100):
  return [[h for i in xrange(M)] for j in xrange(N)]

def reset(d, h=100):
  for i in range(len(d)):
    for j in range(len(d[i])):
      d[i][j] = h
  return d

def input(filename):
  dset = new_dset()
  f = open(filename)
  num = int(f.readline().strip())
  for i in range(num):
    N, M = (int(s) for s in f.readline().strip().split(' '))
    dset = reset(dset) # change this XXX
    for j in range(N):
      line = f.readline().strip().split(' ')
      for k in range(M):
        dset[j][k] = int(line[k])
    yield dset, N, M

def do_work(d, N, M):
  N_max = [0 for i in xrange(N)]
  M_max = [0 for i in xrange(M)]
  #print_dset(dset, N, M)
  
  for i in xrange(N):
    for j in xrange(M):
      if N_max[i] < d[i][j]:
        N_max[i] = d[i][j]

  for j in xrange(M):
    for i in xrange(N):
      #print 'i j N M d', i, j, N, M, d[i][j]
      if M_max[j] < d[i][j]:
        M_max[j] = d[i][j]
  #print 'maxes', N_max, M_max
  
  for i in xrange(N):
    for j in xrange(M):
      if d[i][j] < N_max[i] and d[i][j] < M_max[j]:
        return 'NO'

  return 'YES'


if __name__ == '__main__':
  gen = input(sys.argv[1])
  for i, (dset, N, M) in enumerate(gen):
    print 'Case #%s: %s' % (i+1, do_work(dset, N, M))
