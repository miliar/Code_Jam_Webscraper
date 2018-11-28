import string
import array
import copy

def propagate(neighbors, dx, dy):
#  print "propagating with dx=%d and dy=%d" % (dx, dy)
  for y in xrange(4-dy) if dy >=0 else range(3, 0, dy):
    for x in xrange(4-dx) if dx >= 0 else range(3, 0, dy):
      me = neighbors[y*4+x]
#      print "Looking at %d at (%d, %d)" % (me, x, y)
      if me >= 1:
#        print "Got %d at %d and %d" % (me, x, y)
        if neighbors[(y+dy)*4+x+dx] != 0: 
          neighbors[(y+dy)*4+x+dx] += me


def isThisSideWinning(arr, ch):
#  print arr
  neighbors = array.array('i')
  for line in arr:
    for c in line:
      neighbors.append(1 if (c == ch or c == 'T') else 0)
#  print neighbors

  c = copy.copy(neighbors)
  propagate(c, 1, 0)
#  print c
  if 4 in c:
    return '%c won' % ch
#  print "---"

  c = copy.copy(neighbors)
  propagate(c, 1, -1)
#  print c
  if 4 in c:
    return '%c won' % ch
#  print "---"

  c = copy.copy(neighbors)
  propagate(c, 0, 1)
#  print c
  if 4 in c:
    return '%c won' % ch
#  print "---"

  c = copy.copy(neighbors)
  propagate(c, 1, 1)
#  print c
  if 4 in c:
    return '%c won' % ch
#  print "---"

def determineStatus(arr):
  isXWinnning = isThisSideWinning(arr, 'X')
  if isXWinnning: return isXWinnning

  isOWinning = isThisSideWinning(arr, 'O')
  if isOWinning: return isOWinning

  for line in arr:
    if line.find('.') != -1:
      return 'Game has not completed'

  return 'Draw'

f = open('problem1', 'r')
results = []
nproblems = int(f.readline())
while nproblems > 0:
  arr = []

  for i in xrange(4):
  	arr.append(f.readline()[0:4])

  f.readline()

#  print arr
  result = determineStatus(arr)
#  print result
  results.append('Case #%s: %s' % (len(results)+1, result))
  nproblems = nproblems - 1

for result in results:
  print result