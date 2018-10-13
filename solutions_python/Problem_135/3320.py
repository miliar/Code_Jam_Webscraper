#!/usr/bin/env python

import sys
data = open(sys.argv[1], 'r').read()
data = data.split('\n')
data.reverse()
T = int(data.pop())

for i in xrange(T):
  firstLineNr = int(data.pop())
  firstLine = [data.pop(), data.pop(), data.pop(), data.pop()][firstLineNr - 1]

  secondLineNr = int(data.pop())
  secondLine = [data.pop(), data.pop(), data.pop(), data.pop()][secondLineNr - 1]

  same = set(firstLine.split(' ')).intersection(set(secondLine.split(' ')))
  if len(same) is 1:
    result = same.pop()
  elif len(same) is 0:
    result = 'Volunteer cheated!'
  else:
    result = 'Bad magician!'

  print 'Case #%s: %s' % (i + 1, result)
