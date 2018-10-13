#!/usr/bin/env python3
import fileinput

def solve(c, f, x):
  best_time = float("inf")
  current_time = 0
  rate = 2
  while current_time < best_time:
    new_time = current_time + x / rate
    best_time = min(best_time, new_time)
    current_time += c / rate
    rate += f
  return best_time

if __name__ == '__main__':
  with fileinput.input() as f:
    tests = int(next(f))
    for t in range(1, tests + 1):
      answer = solve(*map(float, next(f).split()))
      print("Case #{t}: {answer}".format(t=t, answer=answer))
