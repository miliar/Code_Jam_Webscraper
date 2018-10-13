import sys

tc = int(input())
for t in range(tc):
  x = int(input())
  a = [input().split() for _ in range(4)]
  y = int(input())
  b = [input().split() for _ in range(4)]
  z = set(a[x-1]) & set(b[y-1])
  if not z:
    print("Case #{}: Volunteer cheated!".format(t+1))
  elif len(z) > 1:
    print("Case #{}: Bad magician!".format(t+1))
  else:
    print("Case #{}: {}".format(t+1, z.pop()))

