#!/usr/bin/env python

import sys

def main():
  fi = sys.stdin
  fo = sys.stdout
  caseCount = int(fi.readline().strip())
  for i in xrange(1, caseCount+1):
    n, words = readInput(fi)
    moves = solve(n, words)
    displayAndClear(fo, i, moves)

def readInput(f):
  n = int(f.readline().strip())
  words = [f.readline().strip() for i in xrange(n)]
  return n, words

def displayAndClear(f, i, moves):
  if moves == -1:
    f.write('Case #%d: Fegla Won\n' % i)
  else:
    f.write('Case #%d: %d\n' % (i, moves))
  f.flush()

def solve(n, ws):
  r, c1 = compact(ws[0])
  cs = [c1]

  for i in xrange(1, n):
    ri, ci = compact(ws[i])
    if ri != r:
      return -1
    cs.append(ci)

  avgs = [sum([c[i] for c in cs]) for i in xrange(len(r))]
  avgs = [int(round(float(avg)/n)) for avg in avgs]

  moves = 0
  for c in cs:
    for i in xrange(len(r)):
      moves += abs(c[i] - avgs[i])

  return moves

def compact(s):
  r = []
  c = []
  i = 0
  while i < len(s):
    if not r or r[-1] != s[i]:
      r.append(s[i])
      c.append(1)
    else:
      c[-1] += 1
    i+= 1
  return r, c

if __name__ == '__main__':
  main()

