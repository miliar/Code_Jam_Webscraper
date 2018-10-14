ti = 0
tn = input()

while (ti < tn):
  ti += 1
  x, y = raw_input().split()
  k = int(y)
  a = map(lambda xi: xi == '+', x)
  c = 0

  for i in range(len(a) - k + 1):
    if not a[i]:
      c += 1
      for j in range(i, i + k):
        a[j] = not a[j]

  if (not all(x for x in a)): c = -1

  print 'Case #%s: %s' % (ti, c if c != -1 else 'IMPOSSIBLE')

