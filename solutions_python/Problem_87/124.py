for case in xrange(1, int(raw_input())+1):
  X, S, R, t, N = map(int, raw_input().split())
  walkway = [map(int, raw_input().split())[::-1] for _ in xrange(N)]
  walkway_length = sum(w[1] - w[2] for w in walkway)
  walkway.sort()

  non_walkway_run = min(t, (X - walkway_length) / float(R)) * R
  non_walkway_walk = X - walkway_length - non_walkway_run
  ans = float(non_walkway_run) / (R)
  ans += float(non_walkway_walk) / (S)
  t -= float(non_walkway_run) / (R)

  for w in walkway:
    run = min(t, (w[1] - w[2]) / float(w[0] + R)) * (w[0] + R)
    walk = w[1] - w[2] - run
    ans += float(run) / (w[0] + R)
    ans += float(walk) / (w[0] + S)
    t -= float(run) / (w[0] + R)

  print "Case #%d: %f" % (case, ans)
