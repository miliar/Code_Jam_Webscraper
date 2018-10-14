import sys

def bnnle(N):
  s=str(N)
  i=int(s[0])
  n=len(s)
  if n==1: return i
  if i*(10**n-1)//9>N: return i*10**(n-1)-1
  return i*10**(n-1)+bnnle(N-i*10**(n-1))

T=int(sys.stdin.readline())
for case in range(1,T+1):
  N=int(sys.stdin.readline().strip())
  print "Case #%d:"%case,bnnle(N)
