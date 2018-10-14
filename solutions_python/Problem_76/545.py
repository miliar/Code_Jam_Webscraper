#!/usr/bin/python

from sys import stdin

def xor_sum(values):
  xored = 0

  for value in values:
    xored ^= value

  return xored

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices), tuple(pool[i] for i in range(r, n))
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        excluded = set(range(n))
        for i in indices:
          excluded.remove(i)
        yield tuple(pool[i] for i in indices), tuple(pool[i] for i in excluded)

def evaluate_case(n, case):
  values = [int(c) for c in case.split(' ')]
  
  if xor_sum(values):
    return 'NO'

  return str(sum(values) - min(values))
    
cases = stdin.readlines()
count = int(cases[0])

for i in range(1, count+1):
  print('Case #' + str(i) + ': ' + evaluate_case(int(cases[2*i-1]), cases[2*i]))
