for cas in xrange(1,1+input()):
  print "Case #%s:" % cas,
  n = raw_input()
  d = map (int, n)

  b = True
  for i in range(1,len(d)):
    if b:
      if d[i] < d[i-1]:
        b = False
        d[i] = 9
        d[i-1] -= 1

    else:
      d[i] = 9

  for i in reversed(range(1,len(d))):
    if d[i] < d[i-1]:
        d[i] = 9
        d[i-1] -= 1



  print int(''.join(str(i) for i in d))