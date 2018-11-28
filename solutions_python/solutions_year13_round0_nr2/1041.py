#!/usr/bin/python2.7
import sys

MAX = 1000

def process(lines):
  cols = [MAX] * len(lines[0])
  mincols = [0] * len(lines[0])
  for i, line in enumerate(lines):
    local = max(line)
    for j,num in enumerate(line):
      if num == local:
        if (local > cols[j]):
          return "NO"
        mincols[j] = local
        continue
      if cols[j] == MAX:
        if (num < mincols[j]):
          return "NO"
        cols[j] = num
        continue
      if cols[j] != num:
        return "NO"
  return "YES"

def processSmall(lines):
  cols = set()
  idx = 0
  for i, line in enumerate(lines):
    tcols = set()
    for j, num in enumerate(line):
      if num == 1:
        tcols.add(j)
    if (len(tcols) != len(line)):
      cols = tcols
      idx = i + 1
      break
  for i, line in enumerate(lines[idx:]):
    allOnes = True
    for j, num in enumerate(line):
      if allOnes:
        if num == 1:
          continue
        else:
          allOnes = False
          for k in xrange(0,j):
            if not k in cols:
              return "NO"
      if num == 1 and not j in cols:
        return "NO"
      if num == 2 and j in cols:
        return "NO"
  return "YES"

f = open(sys.argv[1])
N = int(f.readline())

for i in xrange(1, N + 1):
  X, Y = map(lambda str: int(str), f.readline().split())
  lines = []
  for j in xrange(0, X):
    line = map(lambda str: int(str), f.readline().split())
    lines.append(line)
  res1 = process(lines)
  print "Case #" + str(i) + ": " + process(lines)
