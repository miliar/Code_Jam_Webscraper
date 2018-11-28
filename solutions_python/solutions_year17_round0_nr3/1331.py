import math

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]
  r = (n - k) / math.pow(2, math.floor(math.log(k, 2) + 1))
  r2 = r
  q = r % 1
  if q >= 0.5:
    r2 += 0.5
  print("Case #{}: {} {}".format(i, int(math.floor(r2)), int(math.floor(r))))
  # check out .format's specification for more formatting options
 
