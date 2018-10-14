import sys
f = sys.stdin
t = int(f.readline())
for i in range(1,t+1):
  n, s = f.readline().split()
  n = int(n)
  s = map(int, s)
  j=0; k=0
  for jj in range(n+1):
    if j<jj and s[jj]>0:
      k+=jj-j
      j+=jj-j
    j+=s[jj]
  print 'Case #%d: %d'%(i,k)


