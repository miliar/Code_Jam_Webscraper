#!/bin/python

import fileinput

def solve(line):
  tokens = line.split(' ')
  N = int(tokens[0])
  S = int(tokens[1])
  p = int(tokens[2])
  result = 0
  for index in range(3, N + 3):
    score = int(tokens[index])
    maxNonSurprising = score / 3
    if (score % 3 != 0):
      maxNonSurprising += 1
    if (maxNonSurprising >= p):
      result += 1
    elif (S > 0 and score > 0 and maxNonSurprising + 1 >= p):
      S -= 1
      result += 1
#    print("%d: %d %d %d" % (index - 3, score, score / 3, maxNonSurprising))
  return result

lines = fileinput.input(files=['dancing.in'])
N = int(lines[0])
for index in range(1, N + 1):
  line = lines[index].rstrip()
  out = solve(line)
  print("Case #%d: %d" % (index, out))
