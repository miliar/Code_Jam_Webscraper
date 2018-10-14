import sys, re

T = int(sys.stdin.readline())

for case_ in range(T):
  N = int(sys.stdin.readline())
  a = [int(n) - 1 for n in sys.stdin.readline()[:-1].split(' ')]
  answer = N
  assert sorted(a) == list(range(N))
  for i in range(N):
     if a[i] == i:
       answer -= 1
  
  print('Case #{0}: {1}.000000'.format(case_ + 1, answer))
