import re, sys

T = int(sys.stdin.readline())

for case_ in range(T):
  C = int(sys.stdin.readline())
  ss = [int(x) for x in sys.stdin.readline()[:-1].split(' ')]
  x = 0
  for s in ss:
    x ^= s

  print('Case #{0}: {1}'.format(case_ + 1, 'NO' if x != 0 else sum(ss) - sorted(ss)[0]))
