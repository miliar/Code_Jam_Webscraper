#!/usr/bin/python4

# Question: http://code.google.com/codejam/contest/dashboard?c=544101#
import string

def makeRow(line):
  _len_line = len(line)
  for i in range(0, _len_line):
    if line[i] == '.':
      RBW_set['W'].append(i + 1 + (table_y * len(table_set)))
    elif line[i] == '#':
      RBW_set['B'].append(i + 1 + (table_y * len(table_set)))
  print RBW_set
  table_set.append(line)

def isItPossible(rblist):
  tiles = [i for i in rblist]
  t_temp = []
  line = list(string.join(table_set, ''))
  for tile in tiles:
    if tile in t_temp:
      continue
    cur = tile
    temp = [cur]
    if cur + 1 in tiles:
      temp.append(cur + 1)
    if cur + table_y in tiles:
      temp.append(cur + table_y)
    if cur + table_y + 1 in tiles:
      temp.append(cur + table_y + 1)
    if len(temp) == 4:
      cnt = 0
      for i in temp:
        ind = rblist.index(i)
        a = rblist[ind]
        del line[a - 1]
        if cnt == 0 or cnt == 3:
          line.insert(a - 1, '/')
        else:
          line.insert(a - 1, '\\')
        cnt += 1
        t_temp.append(i)
        del rblist[ind]
  print RBW_set['B']
  print line
  if len(RBW_set['B']) > 0:
    return 'Impossible'
  else:
    s = ''
    ln = len(line)
    for i in xrange(ln):
      s += line[i]
      if (i + 1) % table_y == 0 and (i + 1) != ln:
        s += '\n'
    return s


fname = 'test'
f = open('%s.in' % fname, 'r')
cnt = 0
result = []
table_x = 0
table_y = 0
table_set = []
RBW_set = {'R': [],
          'B': [],
          'W': []}
for line in f.readlines():
  if not cnt:
    cnt += 1
    continue
  if not table_x or not table_y:
    table_x, table_y = [int(i) for i in line.replace('\n', '').split(' ')]
    continue
  if len(table_set) != table_x - 1:
    makeRow(line.replace('\n', ''))
    continue
  makeRow(line.replace('\n', ''))
  result.append('Case #%s:\n%s' % (cnt, isItPossible(RBW_set['B'])))
  table_x, table_y = 0, 0
  table_set = []
  RBW_set = {'R': [],
            'B': [],
            'W': []}
  print '-------------'
  cnt += 1
f.close()
f = open('%s.out' % fname, 'w')
f.write(string.join(result, '\n'))
f.close()
print string.join(result, '\n')
