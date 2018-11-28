from math import ceil
for t in range(input()):
  n, p = map(int, raw_input().split())
  req = map(int, raw_input().split())
  q = [sorted(map(int, raw_input().split())) for _ in range(n)]
  minserv = lambda a, r: int(ceil(a / (1.1 * r)))
  maxserv = lambda a, r: int(a / (0.9 * r))
  res = 0
  while all(map(len, q)):
    minservs = [minserv(q[i][0], req[i]) for i in range(n)]
    maxservs = [maxserv(q[i][0], req[i]) for i in range(n)]
    if max(minservs) <= min(maxservs):
      q = [r[1:] for r in q]
      res += 1
    else:
      x = max(minservs)
      q = [r[1:] if maxservs[i] < x else r for i, r in enumerate(q)]
  print 'Case #%d: %d' % (t+1, res)
