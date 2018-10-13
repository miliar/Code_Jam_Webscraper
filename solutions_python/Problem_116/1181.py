#!/usr/bin/env python
import sys, re

try:
  f = open(sys.argv[1])
except IOError:
  print "No input file specify, do nothing."
  exit()


pX = r'[XT]{4}'
pO = r'[OT]{4}'
def diag(data, direction):
  if (direction == 'left'):
    return ''.join([data[i][i] for i in range(4)])
  else:
    return ''.join([data[i][3 - i] for i in range(4)])

def solve(data):
  d = data
  t = zip(*data)
  for i in range(4):
    if re.match(pX, ''.join(d[i])) or re.match(pX, ''.join(t[i])):
      return 'X'
    if re.match(pO, ''.join(d[i])) or re.match(pO, ''.join(t[i])):
      return 'O'
    if i is 0:
      if re.match(pX, diag(data, 'left')) or re.match(pX, diag(data, 'left')):
        return 'X'
      if re.match(pO, diag(data, 'left')) or re.match(pO, diag(data, 'left')):
        return 'O'
    if i is 3:
      if re.match(pX, diag(data, 'right')) or re.match(pX, diag(data, 'right')):
        return 'X'
      if re.match(pO, diag(data, 'right')) or re.match(pO, diag(data, 'right')):
        return 'O'

  cX = cO = cP = cT = 0
  for i in d:
    for j in i:
      cX = cX + (1 if j is 'X' else 0)
      cO = cO + (1 if j is 'O' else 0)
      cP = cP + (1 if j is '.' else 0)
      cT = cT + (1 if j is 'T' else 0)

  #if ((cT + cO < cX) or (cP > cT + cX + cO):
  if cP > 0:
    return 'N'

  return 'D'

ns = int(f.readline())
for i in range(ns):
  data = [[k for k in f.readline().strip()] for j in range(4)]
  f.readline()
  result = solve(data)
  if result is 'X' or result is 'O':
    print "Case #%d: %s won" % (i + 1, result)
  elif result is not 'D':
    print "Case #%d: Game has not completed" % (i + 1)
  else:
    print "Case #%d: Draw" % (i + 1)
