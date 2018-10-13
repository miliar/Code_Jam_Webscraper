#!/usr/bin/env python

import sys

def parse(fname):
  f = open(fname, 'r')
  inputs = list()
  lines = f.readlines()
  n = int(lines[0])
  lines = lines[1:]

  for i in xrange(n):
    ansA = int(lines[10 * i])
    ansB = int(lines[10 * i + 5])
    gridA = list(list(int(x) for x in line.split()) for line in lines[10 * i + 1:10 * i + 5])
    gridB = list(list(int(x) for x in line.split()) for line in lines[10 * i + 6:10 * i + 10])
    inputs.append((gridA, ansA, gridB, ansB))

  return inputs


def solve(gridA, ansA, gridB, ansB):
  possible = set(gridA[ansA - 1]) & set(gridB[ansB - 1])
  if len(possible) == 0:
    return "Volunteer cheated!"
  elif len(possible) == 1:
    return possible.pop()
  else:
    return "Bad magician!"

if __name__ == '__main__':
    fname = sys.argv[1]
    lines = list()
    inputs = parse(fname)
    for i,input in enumerate(inputs):
        lines.append('Case #%d: %s\n' % (i + 1, solve(*input)))
    outFile = open(fname.replace('.in', '.out'), 'w')
    outFile.writelines(lines)
    outFile.close()

