import os
import math

def one_round(number):
  for i in range(len(number)-1):
    if number[i] > number[i+1]:
      number[i] -= 1
      for j in range(i+1, len(number)):
        number[j] = '9'
      return True, number
  return False, number

def solve(number):
  while True:
    has_change, number = one_round(number)
    if not has_change:
      break

  for i in range(len(number)):
    if chr(number[i]) != '0':
      number = number[i:]
      break
  return str(number)

fin = open('B-large.in', 'r')
fout = open('B.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  line = line.strip()

  number = bytearray(line)
  res = solve(number)

  out_str = 'Case #%d: %s\n' % (i, res)
  print out_str
  fout.write(out_str)
fin.close()
fout.close()

