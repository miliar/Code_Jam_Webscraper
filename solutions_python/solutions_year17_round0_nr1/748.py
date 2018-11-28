import os
import math

def solve(pancake, size):
  times = 0
  for left in range(0, len(pancake) - size + 1):
    if chr(pancake[left]) == '-':
      times += 1
      for i in range(left, left+size):
        pancake[i] = '+' if chr(pancake[i]) == '-' else '-'

  print pancake
  for c in pancake:
    if chr(c) == '-':
      return 'IMPOSSIBLE'
  return times

fin = open('A-large.in', 'r')
fout = open('A.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  line = line.strip()

  pancake, size = line.split()
  pancake = bytearray(pancake)
  size = int(size)

  res = solve(pancake, size)

  out_str = 'Case #%d: %s\n' % (i, res)
  print out_str
  fout.write(out_str)
fin.close()
fout.close()

