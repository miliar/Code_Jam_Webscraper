def flip(a, i):
  for j in range(i, len(a)):
    a[j] = 9
  return a

def solve(x):
  a = []
  while x > 0:
    a = [x % 10] + a
    x //= 10
  for i in range(len(a)-2, -1, -1):
    if a[i] > a[i+1]:
      a = flip(a, i+1)
      a[i] -= 1

  x = 0
  mag = 0
  for i in range(len(a)-1, -1, -1):
    x += a[i]*(10**mag)
    mag += 1
  return x

T = int(input())

for TT in range(T):
  res = solve(int(input()))
  print("Case #{}: {}".format(TT + 1, res))
