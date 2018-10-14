import math

t = int(input())  # read a line with a single integer

def get_pissuars(n, k):
  log2k = math.log2(k)
  e2 = math.pow(2, math.floor(log2k))
  e21 = math.pow(2, math.floor(log2k+1))
  mx = (n - k + e2) // e21
  mn = (n - k) // e21
  return int(mx), int(mn)

for c in range(1, t + 1):
  n, k = map(int, input().split())
  r = get_pissuars(n, k)
  print("Case #{}: {} {}".format(c, *r))
