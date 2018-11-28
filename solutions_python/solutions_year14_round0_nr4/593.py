def score(a, b):
  a = a[:]
  b = b[:]
  s = 0
  while a:
    high = a.pop()
    for ind, weight in enumerate(b):
      if weight > high:
        b.pop(ind)
        break
    else:
      s += 1
      b.pop(0)
  return s

for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  N = input()
  naomi = sorted(map(float, raw_input().split()))
  ken = sorted(map(float, raw_input().split()))
  print N - score(ken, naomi), score(naomi, ken)

