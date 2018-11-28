from fractions import gcd

s = open('C-small-attempt0.in','r').read()
out = open('C-small.out','w')

new = s.split('\n')
#print new

n = 0
i = 0
R = 0
k = 0
N = 0
G = [0]

for s in new:
  if n == 0:
    n = int(s)
    continue
  
  s = s.split(' ')
  if len(s) < 1:
    break
  
  if len(G) == 0:
    for c in s:
      G.append(int(c))
    i += 1 
  else:
    [R,k,N] = [int(c) for c in s]
    G = []
    continue
  
#  print R,k,N,G  
  cnt = 0
  K = 0
  tmp = []
  A = 0
  B = 0
  a = sum(G)
  new = 0
  if a < k:
    new = k/a
    cnt = new*a  
    
  for r in xrange(R-new):
    #print r,A,B,G
    while K+G[B] <= k:    
      K += G[B]
      B = (B+1)%N
      if A == B:
        break
    A = B
    cnt += K
    K = 0
    
  out.write("Case #" +str(i)+": "+str(cnt)+"\n")
  
  n = n-1
#  print n
  if n == 0:
    break
