import sys

def run(t):
  A, B, K = map(int, raw_input().split())
  result = 0
  for a in range(0, A):
    for b in range(0, B):
      if a & b < K:
        result += 1
  print('Case #{}: {}'.format(t, result))

T = int(raw_input())
for t in xrange(1, T + 1):
  run(t)
