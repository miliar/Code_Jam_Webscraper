from collections import defaultdict

T = int(raw_input(""))

for t in range(1,T+1):
  N, K = map(int, raw_input("").split(" "))
  d = defaultdict(lambda: 0)
  d[N] = 1
  for k in range(K-1):
    m = max(k for k, v in d.iteritems() if v!= 0)
    d[m] -= 1
    l = int(m/2)
    r = 0
    if (m-1)%2 == 0:
      r = l
    else:
      r = l-1
    d[l] += 1
    d[r] += 1

  m = max(k for k, v in d.iteritems() if v!=0)
  l = int(m/2)
  r = 0
  if (m-1)%2 == 0:
    r = l
  else:
    r = l-1
  print "Case #%d: %d %d" % (t, max(l,r), min(l,r))
