from collections import defaultdict

def simlist(lst):
  t = sorted(lst)
  ret = []
  for elm in lst:
    for i in xrange(len(lst)):
      if t[i] == elm: ret.append(i)
  return ret

def solve(tcase):
  n = int(raw_input())
  lst = [int(t) for t in raw_input().split()]
  lst = simlist(lst)
  maxn, maxp = -1, -1
  
  lst2 = sorted(lst)

  print 'Case #%d: %d' % (tcase, ans)

T = int(raw_input())
for tcase in xrange(1, T + 1):
  solve(tcase)
