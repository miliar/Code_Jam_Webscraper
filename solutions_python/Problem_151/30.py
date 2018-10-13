import string
from itertools import product

f = open('D-small-attempt0.in', 'r')
#f = open('C-small-attempt0.in', 'r')

T = int(f.readline())

def prefixes(s):
    return set([s[:i] for i in xrange(len(s)+1)])

for test in range(1, T+1):
  M, N = map(int, f.readline().split())
  
  S = [f.readline()[:-1] for i in xrange(M)]
  prsets = [prefixes(s) for s in S]
  
  maxval = 0
  numocc = 0
  
  for assign in product(range(N), repeat=M):
      servers = [set() for i in xrange(N)]
      for i in xrange(M):
          servers[assign[i]] |= prsets[i]
      
      
      
      val = sum([len(server) for server in servers])
      if val > maxval:
          maxval = val
          numocc = 1
      elif val == maxval:
          numocc += 1


  
  print 'Case #' + str(test) + ': ' + str(maxval) + ' ' + str(numocc)
