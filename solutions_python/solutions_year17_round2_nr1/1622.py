t=int(input())
for i in range(1,t+1):
  d,n=[int(x) for x in input().strip().split()]
  a=[]
  for j in range(n):
    dj,sj=[int(x) for x in input().strip().split()]
    a.append((d-dj)/sj)
  print("Case #{:d}: {:.6f}".format(i,d/max(a)))
  
