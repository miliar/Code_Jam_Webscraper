for i in range(int(input())):
  d,n = list(map(int,input().split()))
  t = []
  for j in range(n):
    k,s = list(map(int,input().split()))
    t1 = float(d-k)/s
    t.append(t1)
  print("Case #%d: %f"%(i+1,d/max(t)))