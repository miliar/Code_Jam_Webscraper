#!/usr/bin/python

MODULUS = 10000

def num_welcomes(s, i, target, j, cache):
  if j >= len(target):
    return 1
  if (i, j) in cache:
    return cache[(i, j)]
  num = 0
  ind = s.find(target[j], i)
  while ind != -1:
    num += num_welcomes(s, ind + 1, target, j + 1, cache)
    num = num % MODULUS
    ind = s.find(target[j], ind + 1)
  cache[(i, j)] = num
  return num

f = open('C-small-attempt0.in', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

N = int(lines[0])
target = 'welcome to code jam'

f = open('C-small.out', 'w')
for case in xrange(1, N + 1):
  s = lines[case]
  cache = {}
  s = filter(lambda l: l in target, s)
  ans = num_welcomes(s, 0, target, 0, cache)
  print ans
  f.write('Case #%d: %04d\n' % (case, ans))
f.close()
