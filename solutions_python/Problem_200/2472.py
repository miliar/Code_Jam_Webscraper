n = int(raw_input())
for _, c in enumerate(xrange(n)):
  x = list(map(int, raw_input()))
  nines = 0
  d = len(x)
  for i in xrange(1, len(x)):
    j = len(x) - i - 1
    if x[j] > x[j + 1]:
      nines = i
      d = j + 1
      x[j] = x[j] - 1
  y = ''.join(map(str, x[:d])) + nines * '9'
  if y[0] == '0':
    y = y[1:]
  print 'Case #%d: %s' % (c + 1, y)
