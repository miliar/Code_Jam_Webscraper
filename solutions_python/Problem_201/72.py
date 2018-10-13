import sys

def fast(N,K):
  assert K>0 and K<=N
  if N&1:
    if K==1: return ((N-1)/2,(N-1)/2)
    return fast((N-1)/2,K/2)
  if K==1: return (N/2,N/2-1)
  if K&1: return fast(N/2-1,(K-1)/2)
  return fast(N/2,K/2)

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [N,K]=[int(y) for y in sys.stdin.readline().strip().split()]
  print "Case #%d:"%case,"%d %d"%(fast(N,K))
