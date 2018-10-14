import time

def Bride(Q, i, j):
  m = []
  for q in Q:
    if q >= i and q <= j:
      m.append(j - i + Bride(Q, i, q - 1) + Bride(Q, q + 1, j))
  if m: return min(m)
  else: return 0

for case in xrange(input()):
  (P, Q) = map(int, raw_input().split())
  Q = map(int, raw_input().split())
  print 'Case #%d: %d' % (case + 1, Bride(Q, 1, P))
