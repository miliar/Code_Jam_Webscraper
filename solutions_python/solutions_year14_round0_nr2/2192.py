T = int(raw_input())
for t in range(T):
  C, F, X = raw_input().split()
  C, F, X = float(C), float(F), float(X)

  farmsneeded = 0
  maxtime = X / 2.0
  lasttime = maxtime 
  for n in range(1, int(X / C)+1):
    # before
    f = 2.0 + (n - 1.0) * F
    farmsneeded += C / f
    # after
    f += F
    time = farmsneeded + X / f

    if time < lasttime:
      lasttime = time

  print "Case #%d: %.7f" % (t+1, lasttime)
