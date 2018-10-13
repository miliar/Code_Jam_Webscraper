import sys
from pprint import pprint

def getnums(s):
  return [int(s) for s in s.split() if s.isdigit()]

def nextline():
  return sys.stdin.readline()

def cmprow(field, size, row, num):
  (rows, cols) = size
  for col in range(cols):
    if field[row][col] > num:
      return False
  return True

def cmpcol(field, size, col, num):
  (rows, cols) = size
  for row in range(rows):
    if field[row][col] > num:
      return False
  return True

def totext(b):
  if b: return "YES"
  else: return "NO"

numtests = int(nextline())
for test in range(numtests):
  size = (rows, cols)  = tuple(getnums(nextline()))
  field = []
  for row in range(rows):
    field.append(getnums(nextline()))
  possible = True
  for row in range(rows):
    for col in range(cols):
      if possible:
        possible = (cmpcol(field, size, col, field[row][col]) or cmprow(field, size, row, field[row][col]))

  print 'Case #{}: {}'.format(test+1, totext(possible))




