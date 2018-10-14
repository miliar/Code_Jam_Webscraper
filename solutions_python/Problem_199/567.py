for i in xrange(input()):
  s, n = raw_input().split()
  n = int(n)
  s = list(s)
  l = len(s)
  c = 0
  while '-' in s:
    p = s.index('-')
    if l-p < n:
      break
    for j in xrange(p, p+n):
      s[j] = '+' if s[j] == '-' else '-'
    c += 1
  ans = 'IMPOSSIBLE' if '-' in s else c
  print 'Case #{0}: {1}'.format(i+1, ans)
