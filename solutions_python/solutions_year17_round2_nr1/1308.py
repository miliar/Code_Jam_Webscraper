# A.py Steed 2: Cruise Control
# jreiter

for t in range(int(input())):
  d, n = [int(x) for x in input().split()]
  slowest = -1
 
  for i in range(n):
    k, s = [int(x) for x in input().split()]
    time = (d-k)/s
    if time > slowest:
      slowest = time

  print("Case #{}: {}".format(t+1,  '{0:.6f}'.format(d/slowest)))