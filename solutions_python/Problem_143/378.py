for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  A, B, K = [int(x) for x in raw_input().split()]
  num = 0
  for i in range(A):
    for j in range(B):
      if i&j < K:
        num += 1
  print num

