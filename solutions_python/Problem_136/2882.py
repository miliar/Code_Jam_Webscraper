import sys

tc = int(input())
for t in range(tc):
  rate = 2.0
  c,f,x = map(float, input().split())
  best = 1e9
  time = 0.0
  for i in range(int(x)):
    best = min(best, time + x / rate)
    time += c/rate
    rate += f

  print("Case #{}: {}".format(t+1, best))

