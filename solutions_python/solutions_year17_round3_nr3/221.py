import math

def smallest(PS, N):
  x = PS[0]
  eps = 1e-6
  assert x == min(PS)
  res = [0]
  last = -1
  i = 1
  while i < N and PS[i] <= x + eps:
    res.append(i)
    i += 1
  if i < N:
    last = i

  if last == -1:
    assert len(res) == N
  return res, last

def score(PS, N, K):
  assert N == K
  tot = 1
  for p in PS:
    tot *= p
  return tot




def solve(N, K, U, PS):
  assert N == K
  PS = sorted(PS)
#  print(PS)
  eps = 1e-6
  while U - eps > 0:
    xs, last = smallest(PS, N)
    if last == -1:
      k = U/len(xs)
    else:
      k = min(PS[last]-PS[xs[0]], U/len(xs))
#    print(k, xs)
    for i in xs:
      PS[i] += k
    U -= k*len(xs)
    PS = sorted(PS)
#    print(PS)
  return score(PS, N, K)


T = int(input())
for TT in range(T):
  N, K = map(int, input().split())
  U = float(input())
  PS = map(float, input().split())
  res = solve(N, K, U, PS)
  print("Case #{}: {}".format(TT+1, res))
