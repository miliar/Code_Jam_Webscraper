#!/usr/bin/python4
import string
fname = '/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/C-large'
objfile = open('%s.in' % fname, 'r')
counter = -1
result = []
num = 0
for ln in objfile.readlines():
  counter += 1
  if not counter:
    continue
  if not num:
    num = int(ln.replace('\n', ''))
    counter -= 1 
    continue
  values = [int(i) for i in ln.replace('\n', '').split(' ')]
  fXOR = values[0]
  flag = True
  Scandy = 0
  for i in range(len(values)-1):
    x = fXOR ^ values[i+1]
    fXOR = x
  if x == 0:
    values.sort()
    for j in range(len(values)-1):
      Scandy = Scandy + values[j+1] 
  else:
    flag = False
  result.append('Case #%s: %s' % (counter, str(Scandy) if flag else 'NO'))
  num = 0
objfile.close()
objfile = open('/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/test.out', 'w')
objfile.write(string.join(result, '\n'))
objfile.close()
