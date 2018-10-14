ti = 0
tn = input()

while ti < tn:
  ti += 1
  a = map(int, raw_input())
  n = len(a)

  for i in reversed(range(1, n)):
    if a[i] < a[i - 1]:
      a[i - 1] -= 1
      for j in range(i, n): a[j] = 9

  print 'Case #%s: %d' % (ti, int(''.join(str(x) for x in a)))
