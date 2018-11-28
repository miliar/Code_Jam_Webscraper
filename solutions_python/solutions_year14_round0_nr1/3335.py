import re
import numpy

def readthing(t):
  pos = t.next() - 1
  board = numpy.zeros((4,4))
  for i in range(0,4):
    for j in range(0,4):
      board[i][j] = t.next()
  return pos, board

tokens = [int(x) for x in re.split('\s+', file('magic.in').read()) if x != '']
t = tokens.__iter__()
num_instances = t.next()
for ii in range(0, num_instances):
  i, board1 = readthing(t)
  j, board2 = readthing(t)
  things1 = set(x for x in board1[i,:])
  things2 = set(x for x in board2[j,:])
  intersection = things1 & things2
  if len(intersection) == 0:
    print 'Case #%d: Volunteer cheated!' % (ii+1)
  elif len(intersection) > 1:
    print 'Case #%d: Bad magician!' % (ii+1)
  else:
    for x in intersection:
      print 'Case #%d: %d' % (ii+1, int(x))
