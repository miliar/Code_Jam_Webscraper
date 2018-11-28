for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  C, F, X = map(float, raw_input().split())
  ans = 1e100
  c = 0
  t = 0
  while 1:
    a = t + X / (2 + c*F)
    if a > ans:
      break
    ans = a
    t += C / (2 + c*F)
    c += 1
  print ans
