import math

PI = math.pi

def side(pk):
  return pk[0] * pk[1] * 2 * PI

def top(pk):
  return pk[0] * pk[0] * PI

def solve(zi):
  n, k = input().split()
  n = int(n)
  k = int(k)
  pks = []
  for i in range(n):
    r, h = input().split()
    pks.append((int(r), int(h)))
  pks.sort(key = lambda pk: pk[0] * pk[1], reverse = True)
  #print(n, k)
  #print(pks)
  ans1 = sum(side(pks[i]) for i in range(k)) + max(top(pks[i]) for i in range(k))
  if k < n:
    ans2 = sum(side(pks[i]) for i in range(k-1)) + max(top(pks[i]) + side(pks[i]) for i in range(k, n))
    ans1 = max(ans1, ans2)

  print('Case #%d: %.9f'%(zi+1, ans1))

zn = int(input())
for zi in range(zn):
  solve(zi)
