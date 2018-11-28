npt = [0] + [1 + i*3 for i in xrange(10)]
spt = [0, 0] + [2 + i*3 for i in xrange(9)]

T = int(raw_input())
for case in xrange(T):
  n = [int(i) for i in raw_input().split()]
  N, S, p = n[:3]
  t = list(sorted(n[3:]))

  result = []
  nmin, smin = npt[p], spt[p]
  for x in list(t):
    if x > 1 and x < 29:
      if S > 0 and x >= smin:
        S -= 1
        t.remove(x)
        result.append(x)

  for x in list(t):
    if x >= nmin:
      t.remove(x)
      result.append(x)

  print "Case #%i:" % (case+1), len(result)#, result, N, S, p, t
