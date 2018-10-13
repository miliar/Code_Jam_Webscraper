def flip(S, K):
  f=0
  l=len(S)
  SS=[0]*l
  a=1
  for i in range(0, l):
      if S[i]=='+':
         SS[i]=1
  for i in range(0, l-K+1):
      if SS[i]%2==0:
        f=f+1
        for j in range(0, K):
          SS[i+j]=SS[i+j]+1
  for i in range (l-K,l):
    if SS[i]%2==0:
      a=0
  if a==0:
    return str("IMPOSSIBLE")
  else:
    return f
  

T = int(input())  # read a line with a single integer
S=['']*T
m=['']*T
K=[0]*T
fl=[0]*T

for i in range(0, T ):
  S[i], m[i] = [str(s) for s in input().split(" ")]
  K[i]=int(m[i])

for i in range(0, T ):
  print("Case #{}: {}".format(i+1, flip(S[i], K[i])))
