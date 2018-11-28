from sys import stdin
from collections import defaultdict

T = int(stdin.readline())

for t in range(T):
  N, K = (int(l) for l in stdin.readline().split())
  B = 2 ** (K.bit_length() - 1)
  M = { N : 1 }
  O = None
  while O is None:
    MM = defaultdict(int)
    for R in reversed(sorted(M.keys())):
      if K <= M[R]:
        O = (R // 2, (R - 1) // 2)
        break
      K -= M[R]
      MM[R // 2] += M[R]
      MM[(R - 1) // 2] += M[R]
    M = MM
  (L,R) = O
  print("Case #%d: %d %d" % ((t + 1), L, R))
    
      
    
