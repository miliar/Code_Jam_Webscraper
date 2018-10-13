import sys

input = open(sys.argv[1])
n = int(input.readline())

for nCase in xrange(1, n+1):
  N, K = map(lambda x: int(x), input.readline().split(' ') )
  K = K % 2**N

  #print 'mask  ', format((1<<N)-1, 'b')
  #print 'gadget', format(K, 'b')
  
  print 'Case #%d: %s'%(nCase, 'ON' if K == (1<<N)-1 else 'OFF')
