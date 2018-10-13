tc = raw_input()
tc = int(tc)

for t in xrange(tc):
  n = int(raw_input())
  while n > 0:
    if ''.join(sorted(str(n))) == str(n):
      break
    n -= 1
  print 'Case #' + str(t+1) + ':', n