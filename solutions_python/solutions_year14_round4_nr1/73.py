from collections import defaultdict

def solve(tcase):
  n, x = tuple([int(t) for t in raw_input().split()])
  lst = sorted([int(t) for t in raw_input().split()])
  mp = defaultdict(int)
  for elm in lst:
    mp[elm] += 1

  ans, tot = 0, 0
  while True:
    if tot == n: break
    ans += 1
    a = -1
    for t, c in mp.iteritems():
      if c:
        a = max(a, t)
    mp[a] -= 1
    tot += 1
    if tot == n: break
    b = -1
    for t, c in mp.iteritems():
      if c and t + a <= x:
        b = max(b, t)
    if b != -1:
      mp[b] -= 1
      tot += 1

  print 'Case #%d: %d' % (tcase, ans)

T = int(raw_input())
for tcase in xrange(1, T + 1):
  solve(tcase)
