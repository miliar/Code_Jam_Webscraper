#!/usr/bin/env python

def ans(tbl):
  # by row
  dot = 0
  for i in xrange(4):
    x, o, t = 0, 0, 0
    for j in tbl[i]:
      if j == 'X':
        x = x + 1
      elif j == 'O':
        o = o + 1
      elif j == 'T':
        t = t + 1
      else:
        dot = dot + 1

    if x == 4 or (x == 3 and t == 1):
      return 'X won'
    elif o == 4 or (o == 3 and t == 1):
      return 'O won'

  # by column
  for i in xrange(4):
    x, o, t = 0, 0, 0
    for j in xrange(4):
      c = tbl[j][i]
      if c == 'X':
        x = x + 1
      elif c == 'O':
        o = o + 1
      elif c == 'T':
        t = t + 1
      else:
        dot = dot + 1
    if x == 4 or (x == 3 and t == 1):
      return 'X won'
    elif o == 4 or (o == 3 and t == 1):
      return 'O won'

  x, o, t = 0, 0, 0
  for i in xrange(4):
    if tbl[i][i] == 'X':
      x = x + 1
    elif tbl[i][i] == 'O':
      o = o + 1
    elif tbl[i][i] == 'T':
      t = t + 1
    else:
      dot = dot + 1
  if x == 4 or (x == 3 and t == 1):
    return 'X won'
  elif o == 4 or (o == 3 and t == 1):
    return 'O won'

  x, o, t = 0, 0, 0
  for i in xrange(4):
    if tbl[i][3 - i] == 'X':
      x = x + 1
    elif tbl[i][3 - i] == 'O':
      o = o + 1
    elif tbl[i][3 - i] == 'T':
      t = t + 1
    else:
      dot = dot + 1
  if x == 4 or (x == 3 and t == 1):
    return 'X won'
  elif o == 4 or (o == 3 and t == 1):
    return 'O won'

  if dot == 0:
    return 'Draw'
  else:
    return 'Game has not completed'

def main():
  cases = int(raw_input())
  for case in xrange(cases):
    tbl = []
    for i in xrange(4):
      tbl.append(list(raw_input()))
    raw_input()
    print 'Case #%d: %s' % (case + 1, ans(tbl))

if __name__ == '__main__':
  main()
