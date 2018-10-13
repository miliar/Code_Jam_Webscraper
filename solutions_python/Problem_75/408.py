#!/usr/bin/env python

import re

def solve(cs, ds, ns):
  res = ''
  cs = [(i[0] + i[1], i[1] + i[0], i[2]) for i in cs]
  for n in ns:
    res += n
    if len(res) > 1:
      for c in cs:
        if res[-2:] == c[0] or res[-2:] == c[1]:
          res = res[:-2] + c[2]
          break
    for d in ds:
      if re.search(r'.*'.join(d), res) or re.search(r'.*'.join(reversed(d)), res):
        res = ''
        break
  print '[' + ', '.join([c for c in res]) + ']'

if __name__ == "__main__":
  import sys
  inputFile = file(sys.argv[1], 'r')
  T = int(inputFile.readline())
  testCases = [line.split() for line in inputFile.readlines()]
  inputFile.close()

  for i in range(0, T):
    sys.stdout.write('Case #%d: ' % (i+1))
    testCases[i].reverse()
    C = int(testCases[i].pop())
    cs = [[c for c in testCases[i].pop()] for j in range(0, C)]
    D = int(testCases[i].pop())
    ds = [[d for d in testCases[i].pop()] for j in range(0, D)]
    N = int(testCases[i].pop())
    ns = [j for j in testCases[i].pop()]
    solve(cs, ds, ns)
