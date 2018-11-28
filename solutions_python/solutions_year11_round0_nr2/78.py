import sys
from collections import defaultdict

T = int(sys.stdin.readline())
for test in xrange(T):
  s = sys.stdin.readline().split()
  n = int(s[0])
  m = int(s[n + 1])
  k = int(s[n + m + 2])
  dex = {}
  for x in xrange(n):
    dex[s[x + 1][:2]] = s[x + 1][2]
    dex[s[x + 1][-2:-4:-1]] = s[x + 1][2]
  opp = defaultdict(set)
  for x in xrange(m):
    opp[s[x + n + 2][0]].add(s[x + n + 2][1])
    opp[s[x + n + 2][1]].add(s[x + n + 2][0])
  res = []
  for c in s[-1]:
    if len(res) and (c + res[-1]) in dex:
      res[-1] = dex[c + res[-1]]
    elif set(res).intersection(opp[c]):
      res = []
    else:
      res.append(c)
  print 'Case #%s: [%s]' % (test + 1, ', '.join(res))
