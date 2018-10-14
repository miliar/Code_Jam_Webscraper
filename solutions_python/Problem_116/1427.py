import sys
sys.setrecursionlimit(10000)
n=4
def win(a,p):
  return row(a,p) or col(a,p) or diag(a,p)

def row(a,p):
  won = False
  for i in range(n):
    hit = True
    for j in range(n):
      hit &= a[i][j] in p+'T'
    won |= hit
  return won

def col(a,p):
  won = False
  for j in range(n):
    hit = True
    for i in range(n):
      hit &= a[i][j] in p+'T'
    won |= hit
  return won
    
def diag(a,p):
  won = False
  hit = True
  for k in range(n):
    hit &= a[k][k] in p+'T'
  won |= hit
  hit = True
  for k in range(n):
    hit &= a[k][n-1-k] in p+'T'
  won |= hit
  return won

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  a = [raw_input() for i in range(n)]
  raw_input()
  emptyCells = False
  for i in range(n):
    emptyCells |= '.' in a[i]
  somebodyWins = False
  res = ''
  for p in 'OX':
    if win(a,p):
      res = '%s won' % p
      somebodyWins = True
  if not somebodyWins:
    if emptyCells:
      res = 'Game has not completed'
    else:
      res = 'Draw'
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')

