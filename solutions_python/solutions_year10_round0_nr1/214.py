for case in xrange(1, int(raw_input())+1):
  N, K = map(int, raw_input().split())
  print "Case #%d: %s" % (case, "OFF" if (K+1)%(2**N) else "ON")
