#!/usr/bin/env python
import sys

def readline(): return sys.stdin.readline().strip()
def readrow(): return readline().split(' ')
def addToTable(d, k1, k2, v): 
  di = d.get(k1, {})
  di[k2] = v
  d[k1] = di

T = int(readline())
for t in range(T):
  row = readrow()
  C = int(row[0])
  del row[0]
  combineTable = {}
  for c in range(C):
    a = [x for x in row[c]]
    addToTable(combineTable, a[0], a[1], a[2])
    addToTable(combineTable, a[1], a[0], a[2])
  del row[:C]
  #print combineTable

  D = int(row[0])
  del row[0]
  opposeTable = {}
  for d in range(D):
    a = [x for x in row[d]]
    opposeTable[a[0]] = a[1]
    opposeTable[a[1]] = a[0]
  del row[:D]
  #print opposeTable

  del row[0]
  l = []
  for c in row[0]:
    l.append(c)
    if len(l) >= 2:
      combined = combineTable.get(l[-2], {}).get(l[-1], None)
      if combined is not None:
        del l[-2:]
        l.append(combined)
    if len(l) >= 2:
      table = dict(opposeTable)
      opposed = False
      for e in l:
        o = table.get(e, None)
        if o is not None:
          if isinstance(o, bool):
            opposed = True
            break
          else:
            table[o] = True
            del table[e]
      if opposed: l = []
  print 'Case #%d: [%s]' % (t+1, ', '.join(l))


