#!/usr/bin/python3

import sys
import functools
import operator
import random

def calc(min_k, probs):
  n = len(probs)
  dp = []
  for _ in range(n+1):
    dp.append([0.0] * (n + 1))
  dp[0][0] = 1.0
  for k in range(n+1):
    for i in range(1,n+1):
      p = 0.0
      p += dp[k][i-1] * (1.0 - probs[i-1])
      if k > 0:
        p += dp[k-1][i-1] * probs[i-1]

      dp[k][i] = p

  res = 0.0
  for k in range(min_k, n+1):
    res += dp[k][n]
  return res


def fill_up(probs, U, start_index):
  n = len(probs)
  training_left = U
  for i in range(start_index, n):
    if i + 1 < n:
      d = probs[i+1] - probs[i]
    else:
      d = 1.0 - probs[i]
    add = min(d, training_left / (i - start_index + 1))
    for k in range(start_index, i+1):
      probs[k] += add
      training_left -= add
    if training_left <= 0.0:
      break;
  return probs

def fill_down_partial(probs, U):
  n = len(probs)
  training_left = U
  for i in range(n-1, -1, -1):
    if probs[i] + training_left >= 1.0:
      training_left -= 1.0 - probs[i]
      probs[i] = 1.0
    if training_left <= 0.0:
      break
  return probs

def solve(K, U, probs):
  n = len(probs)
  best_prob = 0.0
  for fill_down in [False, True]:
    p = sorted(list(probs))
    training_left = U
    if fill_down:
      p = fill_down_partial(p, training_left)
      training_left = sum(probs) + U - sum(p)
    for start_index in range(n):
      t = fill_up(list(p), training_left, start_index)
      best_prob = max(best_prob, calc(K, t))
  return best_prob

def token_generator(f):
  for line in f:
    for token in line.split():
      yield token

if __name__ == '__main__':
  in_iter = token_generator(sys.stdin)

  test_cases = int(next(in_iter))

  for test in range(test_cases):
    N = int(next(in_iter))
    K = int(next(in_iter))
    U = float(next(in_iter))
    probs = [float(next(in_iter)) for _ in range(N)]
    result = solve(K, U, probs)
    print('Case #{0}: {1}'.format(test + 1, format(result,'.6f')))

  exit(0)
