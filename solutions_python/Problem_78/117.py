#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

W = []
for i in range(0, 100):
  if i == 0 or 100 % i != 0:
    W.append([])
    continue
  unit = 100 / i
  data = []
  cur = 0
  while cur <= 100:
    data.append(cur)
    cur += unit
  W.append(data)

case = int(sys.stdin.readline())
for c in range(0, case):
  data = sys.stdin.readline().strip().split(' ')
  (N, P_D, P_G) = [int(elem) for elem in data]
  possible = False
  if N >= 100:
    possible = True
  else:
    for i in range(1, N+1):
      target = W[i]
      if P_D in target:
        possible = True
        break
  if possible:
    if P_G == 100 and P_D != 100:
      possible = False
    elif P_G == 0 and P_D != 0:
      possible = False

  print "Case #%d: %s" % (c+1, 'Possible' if possible else 'Broken')

