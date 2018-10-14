from functools import *

def end(t,c):
  print('Case #' + str(t) + ': ', end='')
  if (c in ['X','O']):
    print(c + ' won')
  elif c == 'D':
    print('Draw')
  elif c == '.':
    print('Game has not completed')

def t(c):
  if (c == 'T'):
    return 'Z'
  else:
    return c

def combine(a,b):
  if (a == b):
    return a
  minc = min(t(a), t(b))
  maxc = max(t(a), t(b))
  if (maxc == 'Z'):
    return minc
  elif (minc == 'O'):
    return 'D'
  return minc #'.'

def endCombine(a,b):
  mc = max(a,b)
  if (mc in ['X','O']):
    return mc
  return min(a,b)

testcases = int(input())
for tc in range(1, testcases + 1):
  results = []
  rows = []
  for y in range(0, 4):
    row = input()
    rows.append(row)
    row_char = reduce(combine,row)
    results.append(row_char)
  for col in zip(*rows):
    col_char = reduce(combine,col)
    results.append(col_char)
  diag1 = [rows[i][i] for i in range(4)]
  results.append(reduce(combine, diag1))
  diag2 = [rows[3-i][i] for i in range(4)]
  results.append(reduce(combine, diag2))
#  for x in results:
#    print(x)
  end_state = reduce(endCombine,results)
  end(tc,end_state)

  #Eat trailing new lines
  input()
