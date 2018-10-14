#!/usr/bin/python4
import string
filename = '/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/D-large'
objfile = open('%s.in' % filename, 'r')
counter = -1
res = []
intNum = 0
for ln in objfile.readlines():
  counter += 1
  if not counter:
    continue
  if not intNum:
    intNum = int(ln.replace('\n', ''))
    counter -= 1
    continue
  ln = ln.replace('\n', '').split(' ')
  intNumSum1 = [int(i) for i in ln]
  intNumSum2 = [int(i) for i in ln]
  intNumSum2.sort()
  intHits = 0
  for i in range(0, intNum):
    if intNumSum1[i] != intNumSum2[i]:
      intHits += 1
  res.append('Case #%s: %s' % (counter, intHits))
  intNum = 0
objfile.close()
objfile = open('/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/test.out', 'w')
objfile.write(string.join(res, '\n'))
objfile.close()
