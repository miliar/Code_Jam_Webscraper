#!/usr/bin/python4
import string
fname = '/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/C-small-attempt1'
f = open('%s.in' % fname, 'r')
cnt = -1
result = []
num = 0
for line in f.readlines():
  cnt += 1
  if not cnt:
    continue
  if not num:
    num = int(line.replace('\n', ''))
    cnt -= 1 
    continue
  values = [int(i) for i in line.replace('\n', '').split(' ')]
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
  result.append('Case #%s: %s' % (cnt, str(Scandy) if flag else 'NO'))
  num = 0
f.close()
f = open('/Users/sandeepsawant/Data/EclipseWorkspace/Code jam/src/test.out', 'w')
f.write(string.join(result, '\n'))
f.close()
