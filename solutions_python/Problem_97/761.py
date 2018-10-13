#!/bin/python

import fileinput

def rotate(i, amount):
  result = s[amount:] + s[:amount]
  return result

# returns number of rotations m of n with n < m <= B
def count(n, B, seen):
  rotations = set({})
  s = str(n)
  for i in range(1, 1 + len(s)):
    m = int(s[i:] + s[:i])
    # if m has a leading 0, then n < m will always be false
    if (n < m and m <= B):
      rotations.add(m)
      seen.add(m)
  size = len(rotations)
  result = (size * (size + 1)) / 2
  return result
 
def solve(line):
  seen = set({})
  tokens = line.split(' ')
  A = int(tokens[0])
  B = int(tokens[1])
  result = 0
  for i in range(A, B):
    if not i in seen:
      result += count(i, B, seen)
  return result

lines = fileinput.input(files=['recycled.in'])
N = int(lines[0])
for index in range(1, N + 1):
  line = lines[index].rstrip()
  out = solve(line)
  print("Case #%d: %d" % (index, out))
