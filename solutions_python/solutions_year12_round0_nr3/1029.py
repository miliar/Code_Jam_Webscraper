from collections import deque

def isRecycled(n,m):
  a=n
  b=m
  n=deque([int(i) for i in list(str(n))])
  m=deque([int(i) for i in list(str(m))])

  if(sum(n) != sum(m)):
    return False
  for i in range(len(n)):
    if(n==m):

      return True
    m.rotate(-1)
  return False


f = open('input.dat')
n=f.readline()
n=int(n)



for i in range(n):
  s=f.readline().split(' ')
  count=0
  A=int(s[0])
  B=int(s[1])
  for n in range(A,B):
    for m in range(n+1,B+1):
      if isRecycled(n,m):
        count=count+1
        
  print "Case #"+str(i+1)+": "+str(count)


