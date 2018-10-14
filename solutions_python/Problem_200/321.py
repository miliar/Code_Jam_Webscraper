import sys

T=0
N=0

def read():
  global N
  line=sys.stdin.readline().strip()
  N=int(line)

def solve():
  global N
  if N<10:
    return N
  l=[int(x) for x in list(str(N))]
  l.reverse()

  ans=0
  for i in xrange(len(l)-1):
    if l[i] < l[i+1]:
      for j in xrange(i+1):
        l[j]=9
      l[i+1]-=1 # l[i+1] is not 0
  for i in xrange(len(l)):
    ans+=l[i]*(10**i)
    
  return ans

T=int(sys.stdin.readline())
for i in xrange(T):
  read()
  ans = solve()
  print "Case #{0}: {1}".format(i+1,ans)
