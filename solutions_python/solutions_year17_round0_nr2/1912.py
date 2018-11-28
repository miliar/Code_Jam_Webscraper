from __future__ import print_function
import fileinput

f = fileinput.input()

T = int(f.readline())
for case in range(1, T + 1):
  N = [int(e) for e in f.readline().rstrip()]
  l = len(N)
  for i in range(1, l):
    if N[l-i] < N[l-i-1]:
      for j in range(l-i, l):
        N[j] = 9
      N[l-i-1] -= 1
  print("Case #"+str(case)+": "+"".join(str(e) for e in N).lstrip("0"))
