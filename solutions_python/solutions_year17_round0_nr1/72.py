import sys

def thing(S,K):
  n=0;s=len(S)
  S=[int(x=='+') for x in S]
  for i in range(s-K+1):
    if S[i]==0:
      for j in range(K): S[i+j]=1-S[i+j]
      n+=1
  if S==[1]*s: return n
  else: return "IMPOSSIBLE"

T=int(sys.stdin.readline())
for case in range(1,T+1):
  l=sys.stdin.readline().strip().split()
  print "Case #%d:"%case,thing(l[0],int(l[1]))
