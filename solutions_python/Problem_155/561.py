f=open("A-large.in","r")
g=open("shy.out","w")

T = int(f.readline())

for i in range(0,T):

  [M,s] = f.readline().split()
  N = int(M)
  L = [int(s[j]) for j in range(0,N+1)]
  S = 0
  C = 0
  for k in range(0,N+1):
    if S < k:
      C += 1
      S += 1
    S = S+L[k]

  g.write("Case #"+str(i+1)+": "+str(C)+"\n")

  
  
  
