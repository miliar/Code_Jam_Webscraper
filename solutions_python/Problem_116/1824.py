
import numpy as np

def error(msg=''):
  raise RuntimeError(msg)

def win(table):
  for i in xrange(4):
    if table[i, :].all():
      return True
    if table[:, i].all():
      return True
  if table[0, 0] and table[1, 1] and table[2, 2] and table[3, 3]:
    return True
  if table[0, 3] and table[1, 2] and table[2, 1] and table[3, 0]:
    return True
  return False

f = open('A-small-attempt2.in')

size = int(f.readline())

tableX = np.zeros([4, 4], 'bool')
tableO = np.zeros([4, 4], 'bool')

for i in xrange(size):
  for j in xrange(4):
    has_empty = False
    line = f.readline()
    for k in xrange(4):
      if line[k] == 'X':
        tableX[j, k] = True
        tableO[j, k] = False
      elif line[k] == 'O':
        tableX[j, k] = False
        tableO[j, k] = True
      elif line[k] == 'T':
        tableX[j, k] = True
        tableO[j, k] = True
      elif line[k] == '.':
        has_empty = True
        tableX[j, k] = False
        tableO[j, k] = False
      else:
        error('bad input character')
  f.readline()

  print 'Case #%d: '%(i+1),
  if win(tableX):
    print 'X won'
  elif win(tableO):
    print 'O won'
  elif has_empty:
    print 'Game has not completed'
  else:
    print 'Draw'
  
