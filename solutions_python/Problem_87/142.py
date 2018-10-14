from __future__ import division
gis = lambda: map(int, raw_input().split())
gi = lambda:  gis()[0]
for k in xrange(input()):
  x, s, r, t, n = gis()
  walks = []
  for i in xrange(n):
    b, e, w = gis()
    x -= (e-b)
    walks.append([w, e-b])
  walks.append([0, x])
  walks.sort()
  tt = 0
  for i, (w, l) in enumerate(walks):
    td = min(t, l/(r+w))
    l = s*td + (l-r*td)
    t -= td
    
    tt += l/(s+w)

  print "Case #%d: %.20f" % (k+1, tt)