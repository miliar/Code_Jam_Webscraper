from math import *

def solve(prob):
  f=open(prob+'.in','r')
  out=open(prob+'.out','w')
  
  T = int(f.readline())
  for t in range(T):
    (N,K)=map(int,f.readline().split())
    v = 'OFF'
    for i in range(N):
      if K & 1 == 0: break
      K = K >> 1
    else:
      v = 'ON'
    print >>out,'Case #%d: %s'%(t+1,v)

  f.close()

#  for x in result
  out.close()

#solve(sys.argv[1])
#for i in range(1,11): solve(i)
solve('A-large')