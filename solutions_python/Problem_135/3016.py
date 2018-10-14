n = input()
for r in xrange(n):
  a = input() - 1
  x = [raw_input().split(' ') for i in xrange(4)]
  b = input() - 1
  y = [raw_input().split(' ') for i in xrange(4)]
  t = list(set(x[a]) & set(y[b]))
  print 'Case #' + str(r+1) + ':',
  if len(t) == 0: print 'Volunteer cheated!'
  elif len(t) == 1: print t[0]
  else: print 'Bad magician!'
