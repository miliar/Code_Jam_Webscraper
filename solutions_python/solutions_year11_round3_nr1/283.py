import operator
import itertools
import sys
from sys import stdin

def solve(lines):
  for i in range(0, len(lines)-1):
    for j in range(0, len(lines[i])-1):
      if lines[i][j] == '#':
        if lines[i+1][j] == '#' and \
           lines[i][j+1] == '#' and \
           lines[i+1][j+1] == '#':
          lines[i+1][j] = '\\'
          lines[i][j+1] = '\\'
          lines[i+1][j+1] = '/'
          lines[i][j] = '/'
          continue
        else:
          print "Impossible"
          return
           
  for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
      if lines[i][j] == '#':
        print "Impossible"
        return

  for i in range(0, len(lines)):
    print "".join(lines[i])

f = stdin
#f = open('a.in')
cases = int(f.readline())
for i in xrange(0, cases):
  size = map(int, f.readline().split())

  lines = []
  for j in range(0, size[0]):
    line = []
    for c in f.readline().rstrip():
      line.append(c)
    lines.append(line)

  print 'Case #%d:' % (i+1)
  res = solve(lines)
