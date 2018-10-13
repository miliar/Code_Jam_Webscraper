for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  N, M = map(int, raw_input().split())
  l = []
  orig = 0
  for _ in xrange(M):
    r = map(int, raw_input().split())
    d = r[1]-r[0]
    orig += d * (d-1) / 2 * r[2]
    l.append(r)
  l.sort(reverse=True)
  nu = 0
  while l:
    r = l.pop()
    for s in list(l):
      if r[0] < s[0] and s[0] <= r[1] < s[1]:
        p = min(r[2], s[2])
        if p:
          l.append([r[0], s[1], p])
          l.append([s[0], r[1], p])
          r[2] -= p
          s[2] -= p
    l.sort(reverse=True)
    d = r[1]-r[0]
    nu += d * (d-1) / 2 * r[2]
  print nu - orig
