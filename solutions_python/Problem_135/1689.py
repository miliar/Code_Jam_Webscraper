def solve(tcase):
  r1 = int(raw_input('')) - 1
  m1 = [[int(col) for col in raw_input().split()] for i in xrange(4)]
  r2 = int(raw_input('')) - 1
  m2 = [[int(col) for col in raw_input().split()] for i in xrange(4)]
  ans = []
  for i in xrange(1, 17):
    f = False
    for x in xrange(4):
      if m1[r1][x] == i:
        f = True
        break
    if not f:
      continue
    for x in xrange(4):
      if m2[r2][x] == i:
        f = False
        break
    if not f:
      ans.append(i)
  if len(ans) == 1:
    print 'Case #%d: %d' % (tcase, ans[0])
  elif ans:
    print 'Case #%d: %s' % (tcase, 'Bad magician!')
  else:
    print 'Case #%d: %s' % (tcase, 'Volunteer cheated!')

T = int(raw_input(''))
for tcase in xrange(1, T + 1):
  solve(tcase)