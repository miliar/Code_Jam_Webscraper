t = input()
for c in xrange(t):
  a, b = map(int, raw_input().split())
  res = 0
  for i in range(a, b):
    for j in range(i + 1, b + 1):
      si = str(i)
      sj = str(j)
      if (len(si) == len(sj)):
        si += si
        if si.find(sj) != -1:
          res += 1
  print 'Case #' + str(c+1) + ': ' + str(res)
