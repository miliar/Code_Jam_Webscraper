import sys
inp = sys.stdin

T = int(inp.readline())
for cas in xrange(1, T + 1):
  comb = dict()
  opp = dict()
  parts = inp.readline().strip().split(' ')
  C = int(parts.pop(0))
  for _ in xrange(C):
    c = parts.pop(0)
    comb[tuple(sorted(c[:2]))] = c[2]
  D = int(parts.pop(0))
  for _ in xrange(D):
    d = parts.pop(0)
    opp.setdefault(d[0], set()).add(d[1])
    opp.setdefault(d[1], set()).add(d[0])
  N = int(parts.pop(0))
  elems = parts.pop(0)
  assert N == len(elems)
  l = []
  for e in elems:
    if not l:
      l.append(e)
      continue
    c = tuple(sorted([l[-1], e]))
    if c in comb:
      l.pop()
      l.append(comb[c])
    else:
      for x in l:
        if x in opp.get(e, set()):
          l = []
          break
      else:
        l.append(e)
  print "Case #%d: [%s]" % (cas, ', '.join(l))
