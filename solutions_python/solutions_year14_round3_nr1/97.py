import string

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b,a%b)

T=input()
for t in range(T):
  line=raw_input()
  PQ=string.split(line,'/')
  P=int(PQ[0])
  Q=int(PQ[1])
  D=gcd(Q,P)
  P/=D
  Q/=D
  ans=0
  two=1
  while P*two < Q:
    two *= 2
    ans = ans+1

  ok=False
  two=1
  while two < Q:
    two *= 2
  if two == Q:
    ok=True
  print("Case #"+str((t+1))+": "),
  if ok:
    print(ans)
  else:
    print("impossible")
