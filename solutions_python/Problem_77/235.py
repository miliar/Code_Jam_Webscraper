for case in xrange(1, int(raw_input())+1):
  N = int(raw_input())
  C = map(int, raw_input().split())
  Cs = sorted(C)
  ans = 0
  for i, c in enumerate(C):
    if c != Cs[i]:
      found = False
      for j in xrange(i+1, N):
        if C[j] == Cs[i] and C[j] != Cs[j] and Cs[j] == C[i]:
          found = True
          C[i], C[j] = C[j], C[i]
          ans += 2
          break
      if not found:
        ans += 1

  print "Case #%d: %.8f" % (case, ans)
