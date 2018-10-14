import math

def custom_sort(x):
  r, h = x
  return 2*r*h+r*r

def f(x, cur_r):
  r, h = x
  if r <= cur_r:
    return 2*r*h
  else:
    return 2*r*h+r*r-cur_r*cur_r

def get_score(x, cur_r):
  r, h = x
  if r <= cur_r:
    return math.pi*2*r*h, cur_r
  else:
    return math.pi*(2*r*h+r*r-cur_r*cur_r), r


def solve(N, K, xs):
  xs = sorted(xs, key=lambda x: f(x, 0), reverse=True)
  score, cur_r = get_score(xs[0], 0)
  xs = xs[1:]
  total = score
  K -= 1
  while K > 0:
    xs = sorted(xs, key=lambda x: f(x, cur_r), reverse=True)
    score, cur_r = get_score(xs[0], cur_r)
    xs = xs[1:]
    total += score
    K -= 1
  return total

T = int(input())
for TT in range(T):
  N, K = list(map(int, input().split()))
  xs = []
  for _ in range(N):
    r, h = list(map(int, input().split()))
    xs.append((r, h))
  res = solve(N, K, xs)
  print("Case #{}: {}".format(TT+1, res))
