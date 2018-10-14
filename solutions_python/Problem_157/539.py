#!/usr/bin/env python

import sys

TABLE = {}
POS = 1
NEG = -1
# 1
TABLE['1', '1'] = POS, '1'
TABLE['1', 'i'] = POS, 'i'
TABLE['1', 'j'] = POS, 'j'
TABLE['1', 'k'] = POS, 'k'
# i
TABLE['i', '1'] = POS, 'i'
TABLE['i', 'i'] = NEG, '1'
TABLE['i', 'j'] = POS, 'k'
TABLE['i', 'k'] = NEG, 'j'
# j
TABLE['j', '1'] = POS, 'j'
TABLE['j', 'i'] = NEG, 'k'
TABLE['j', 'j'] = NEG, '1'
TABLE['j', 'k'] = POS, 'i'
# k
TABLE['k', '1'] = POS, 'k'
TABLE['k', 'i'] = POS, 'j'
TABLE['k', 'j'] = NEG, 'i'
TABLE['k', 'k'] = NEG, '1'

def main():
  fi = sys.stdin
  fo = sys.stdout
  caseCount = int(fi.readline().strip())
  for i in range(1, caseCount+1):
    line, x = readInput(fi)
    solution = solve(line, x)
    displayAndClear(fo, i, solution)

def readInput(f):
  _, x = [int(arg) for arg in f.readline().split()]
  line = f.readline().strip()
  return line, x

def displayAndClear(f, i, solution):
  f.write('Case #%d: %s\n' % (i, 'YES' if solution else 'NO'))
  f.flush()

def solve(line, x):
  if len(line) * x < 3:
    return False

  if x > 8:
    x = 8 + (x % 8)
  line = line * x

  mults = [(POS, line[0])]
  for i in xrange(1, len(line)):
    signLast, last = mults[-1]
    signCur, cur = POS, line[i]
    mult = multiply(signLast, last, signCur, cur)
    mults.append(mult)

  if mults[-1] != (NEG, '1'):
    return False

  indI = -1
  for i in xrange(len(mults)):
    if mults[i] == (POS, 'i'):
      indI = i
      break

  indK = -1
  for i in xrange(indI+1, len(mults)):
    if mults[i] == (POS, 'k'):
      indK = i
      break

  if indI >= 0 and indK >= 0:
    return True

  return False


def multiply(signA, a, signB, b):
  signR, r = TABLE[a, b]
  return signA * signB * signR, r

if __name__ == '__main__':
  main()

