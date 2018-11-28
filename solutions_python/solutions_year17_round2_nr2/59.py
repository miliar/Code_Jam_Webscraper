import os
import math

HORSE_NAMES = ['R', 'O', 'Y', 'G', 'B', 'V']

def solve(N, horses):
  ring = []
  last_horse = -1
  for i in range(N):
    max_num = -1
    use_horse = -1
    for jhorse, num in enumerate(horses):
      if num == 0:
        continue
      if last_horse == jhorse:
        continue
      if num > max_num:
        max_num = num
        use_horse = jhorse
      elif num == max_num and i > 0 and jhorse == ring[0]:
        use_horse = jhorse
    if use_horse < 0:
      return 'IMPOSSIBLE'
    ring.append(use_horse)
    horses[use_horse] -= 1
    last_horse = use_horse
  if N > 0 and last_horse == ring[0]:
    return 'IMPOSSIBLE'
  return ''.join([HORSE_NAMES[r] for r in ring])


fin = open('B-small-attempt0 (1).in', 'r')
fout = open('B.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  line = line.strip()

  parts = [int(part) for part in line.split()]
  N = parts[0]
  horses = parts[1:]

  res = solve(N, horses)

  out_str = 'Case #%d: %s\n' % (i, res)
  print out_str
  fout.write(out_str)
fin.close()
fout.close()

