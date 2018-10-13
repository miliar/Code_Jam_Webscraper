#!/usr/bin/env python3

import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for case in range(T):
  L = []
  combine = {}
  opposed = defaultdict(list)

  line = sys.stdin.readline().rstrip('\r\n').split()
  C = int(line[0])
  for combo in line[1:1+C]:
    combine[combo[0],combo[1]] = combo[2]
    combine[combo[1],combo[0]] = combo[2]
    
  D = int(line[1+C])
  for combo in line[2+C:2+C+D]:
    opposed[combo[0]].append(combo[1])
    opposed[combo[1]].append(combo[0])

  [N, S] = line[-2:]

  for c in S:

      L.append(c)
      while len(L)>1 and (L[-2], L[-1]) in combine:
          tmp = combine[L[-2], L[-1]]
          L.pop()
          L.pop()
          L.append(tmp)

      for i in L[::-1]:
          if L[-1] in opposed[i]:
              L = []
              break

    
  s = '[%s]' % ', '.join(map(str, L))
  print('Case #{0}: {1}'.format(case+1, s))
