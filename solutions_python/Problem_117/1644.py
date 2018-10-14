import sys

def checkTable(B, N, M):
  for i in xrange(N):
    for j in xrange(M):
      if B[i][j] != 100:
        return False
  return True

fin = open("in.txt", "r")
f = [int(x) for x in fin.read().split()]
T = f.pop(0)
for k in xrange(T):
  N = f.pop(0) #lines
  M = f.pop(0) #columns
  L = [[f.pop(0) for j in xrange(M)] for i in xrange(N)]
  for h in xrange(100):
    sL = [0 for i in xrange(N)]
    sC = [0 for i in xrange(M)]
    for i in xrange(N):
      for j in xrange(M):
        sL[i] += L[i][j]
        sC[j] += L[i][j]
    for i in xrange(N):
      if sL[i] == h*M:
        for j in xrange(M):
          L[i][j] = h+1
    for j in xrange(M):
      if sC[j] == h*N:
        for i in xrange(N):
          L[i][j] = h+1
         
  if checkTable(L, N, M):
    print "Case #%d: YES" % (k+1)
  else:
    print "Case #%d: NO" % (k+1)
    
