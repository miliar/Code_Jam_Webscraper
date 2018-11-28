#!/usr/bin/python3

import sys
import functools
import operator
import random

def fun1(min_k, poils):
  n = len(poils)
  dp = []
  for _ in range(n+1):
    dp.append([0.0] * (n + 1))
  dp[0][0] = 1.0
  for k in range(n+1):
    for i in range(1,n+1):
      p = 0.0
      p += dp[k][i-1] * (1.0 - poils[i-1])
      if k > 0:
        p += dp[k-1][i-1] * poils[i-1]

      dp[k][i] = p

  res = 0.0
  for k in range(min_k, n+1):
    res += dp[k][n]
  return res


def fill_up(poils, U, start_index):
  n = len(poils)
  poil = U
  for i in range(start_index, n):
    if i + 1 < n:
      d = poils[i+1] - poils[i]
    else:
      d = 1.0 - poils[i]
    add = min(d, poil / (i - start_index + 1))
    for k in range(start_index, i+1):
      poils[k] += add
      poil -= add
    if poil <= 0.0:
      break;
  return poils

def mok_partial(poils, U):
  n = len(poils)
  poil = U
  for i in range(n-1, -1, -1):
    if poils[i] + poil >= 1.0:
      poil -= 1.0 - poils[i]
      poils[i] = 1.0
    if poil <= 0.0:
      break
  return poils

def xkcd(K, U, poils):
  n = len(poils)
  yoK = 0.0
  for mok in [False, True]:
    p = sorted(list(poils))
    poil = U
    if mok:
      p = mok_partial(p, poil)
      poil = sum(poils) + U - sum(p)
    for start_index in range(n):
      t = fill_up(list(p), poil, start_index)
      yoK = max(yoK, fun1(K, t))
  return yoK

def token_generator(f):
  for line in f:
    for token in line.split():
      yield token

if __name__ == '__main__':
  in_iter = token_generator(sys.stdin)

  num_cases = int(next(in_iter))

  for i in range(num_cases):
    N = int(next(in_iter))
    K = int(next(in_iter))
    U = float(next(in_iter))
    poils = [float(next(in_iter)) for _ in range(N)]

    res = xkcd(K, U, poils)

    print('Case #{0}: {1}'.format(i + 1, res))

  exit(0)

