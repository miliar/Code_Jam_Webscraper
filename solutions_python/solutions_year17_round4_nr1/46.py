import os
import math

def solve_2(N, groups):
  count = {0: 0, 1: 0}
  for group in groups:
    if group % 2 == 0:
      count[0] += 1
    else:
      count[1] += 1
  return count[0] + (count[1]+1) / 2

def solve_3(N, groups):
  count = {0: 0, 1: 0, 2:0}
  for group in groups:
    count[group % 3] += 1
  total = count[0]
  temp = min(count[1], count[2])
  total += temp
  count[1] -= temp
  count[2] -= temp
  total += (count[1]+2)/3 + (count[2]+2)/3
  return total

def solve_4(N, groups):
  count = {0: 0, 1: 0, 2:0, 3:0}
  for group in groups:
    count[group % 4] += 1
  total = count[0]
  total += count[2] / 2
  count[2] = count[2] % 2
  temp = min(count[1], count[3])
  total += temp
  count[1] -= temp
  count[3] -= temp
  # 1,1,2
  temp = min(count[1]/2, count[2])
  total += temp
  count[1] -= temp*2
  count[2] -= temp
  # 3,3,2
  temp = min(count[3]/2, count[2])
  total += temp
  count[3] -= temp*2
  count[2] -= temp
  # 1,1,1,1
  total += count[1] / 4
  count[1] = count[1] % 4
  # 3,3,3,3
  total += count[3] / 4
  count[3] = count[3] % 4
  if count[1] or count[2] or count[3]:
    total += 1
  return total


def solve(N, P, groups):
  if P == 2:
    return solve_2(N, groups)
  elif P == 3:
    return solve_3(N, groups)
  elif P == 4:
    return solve_4(N, groups)


fin = open('A-large (2).in', 'r')
fout = open('A.out', 'w')
nown = 0
nowt = 0
t = int(fin.readline())
for nowt in range(t):
  nowt += 1
  line = fin.readline()
  N, P = line.split()
  N = int(N)
  P = int(P)
  groups = []
  line = fin.readline()
  parts = line.split()
  for part in parts:
    groups.append(int(part))

  result = solve(N, P, groups)

  out_str = 'Case #%d: %s\n' % (nowt, result)
  print out_str
  fout.write(out_str)
fin.close()
fout.close()
