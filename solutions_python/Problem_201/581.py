for tc in xrange(input()):
  n, k = map(int, raw_input().split())
  take = [[None, n]]
  d = {n: 1}
  while take:
    temp = set([])
    for x in take:
      temp.add((x[1], x[1]/2))
      if x[1]%2 == 0:
        temp.add((x[1], x[1]/2-1))
    take = filter(lambda x: x[1] != 0, temp)
    for x in take:
      d[x[1]] = d.get(x[1], 0) + d[x[0]]
      if x[0]%2 == 1:
        d[x[1]] += d[x[0]]
  keys = sorted(d.iterkeys(), reverse=True)
  i = p = 0
  while i < k:
    i += d[keys[p]]
    p += 1
  a = b = keys[p-1]/2
  if keys[p-1]%2 == 0:
    b -= 1
  print 'Case #{0}: {1} {2}'.format(tc+1, a, b)
