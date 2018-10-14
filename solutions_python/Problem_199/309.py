import sys

T=0
S=""
K=0

def read():
  global S,K
  line=sys.stdin.readline().strip()
  a=line.split()
  S=list(a[0])
  K=int(a[1])

def solve():
  ans=0
  for i in xrange(len(S)-K+1):
    if S[i]=='+':
      continue
    ans+=1
    for j in xrange(i,i+K):
      if S[j]=='+':
        S[j]='-'
      else:
        S[j]='+'

  #final check
  for i in xrange(len(S)):
    if S[i]!='+':
      return "IMPOSSIBLE"
  return ans

T=int(sys.stdin.readline())
for i in xrange(T):
  read()
  ans = solve()
  print "Case #{0}: {1}".format(i+1,ans)
