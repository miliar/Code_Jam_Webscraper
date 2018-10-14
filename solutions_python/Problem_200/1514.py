
INF = 1000000000

T = int(raw_input().strip())
for _t in xrange(T):
  S = raw_input().strip()
  N = int(S)
  L = len(S)
  S = map(int, list(S))
  T = list(S)
  found = True
  while found:
      found = False
      for i in xrange(1, len(S)):
          if S[i - 1] > S[i]:
              S[i] = 9
              if not(found):
                  S[i - 1] -= 1
              found = True

  print "Case #%d: %s" % (_t + 1, str(int(''.join(map(str, S)))))
