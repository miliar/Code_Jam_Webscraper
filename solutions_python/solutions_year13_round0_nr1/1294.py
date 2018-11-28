import sys
import string
inp = sys.stdin
T = int(inp.readline())

for cas in xrange(1, T + 1):
  print "Case #%d:" % cas,
  tbl = []
  complete = True
  for _ in xrange(4):
    tbl.append(inp.readline().strip())
    if '.' in tbl[-1]:
      complete = False
  inp.readline()
  ttbl = zip(*tbl)
  def lines():
    for row in tbl:
      yield row
    for col in ttbl:
      yield ''.join(col)
    yield ''.join(tbl[x][x] for x in xrange(4))
    yield ''.join(tbl[x][3-x] for x in xrange(4))
  def won(c):
    return (c*4) in (l.replace('T', c) for l in lines())
  if won('X'):
    print "X won"
  elif won('O'):
    print "O won"
  elif complete:
    print "Draw"
  else:
    print "Game has not completed"

