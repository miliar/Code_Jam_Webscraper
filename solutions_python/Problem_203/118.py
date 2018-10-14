import sys

R=0
C=0
B=list()

def read():
  global R,C,B
  line=sys.stdin.readline().strip()
  a=line.split()
  R=int(a[0])
  C=int(a[1])
  B=list()
  for i in xrange(R):
    B.append(list(sys.stdin.readline().strip()))

def solve():
  ans=0
  empty=[True]*R
  for i in xrange(R):
    paint=None
    for j in xrange(C):
      if(B[i][j]=='?'):
        if paint is None:
          pass
        else:
          B[i][j]=paint
      else:
        empty[i]=False
        if paint is None:
          for k in xrange(j+1):
            B[i][k]=B[i][j]
        paint = B[i][j]
  
  paint=None
  for i in xrange(R):
    if empty[i]:
      if paint is None:
        pass
      else:
        B[i]=B[paint]
    else:
      if paint is None:
        for j in xrange(i+1):
          B[j]=B[i]
      paint=i
    


T=int(sys.stdin.readline())
for i in xrange(T):
  read()
  ans = solve()
  print "Case #{0}:".format(i+1)
  for j in B:
    print ''.join(j)
