f=open("B-large.in","r")
g=open("pancakes.out","w")

T = int(f.readline())

for i in range(0,T):
  N = int(f.readline())
  P = sorted(map(int,f.readline().split()))
  m = P[-1]
  ans = m
  for a in range(1,m):
    S = a
    for x in P:
      if x%a == 0:
        S += x/a-1
      else:
        S += x/a
    ans = min(ans,S)

  g.write("Case #"+str(i+1)+": "+str(ans)+"\n")

  
  
  
