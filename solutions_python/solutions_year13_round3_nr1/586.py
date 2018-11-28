for case in xrange(int(raw_input())):
  s, n = raw_input().split()
  L = len(s)
  n = int(n)
  res = 0
  for i, e in enumerate(s):
    cnt, mx = 0, 0
    for j in xrange(i, L):
      if not s[j] in 'aiueo':
        cnt += 1
      else:
        cnt = 0
      mx = max(mx, cnt)
      if n <= mx:
        res += 1
  print 'Case #%d: %d' % (case+1, res)
