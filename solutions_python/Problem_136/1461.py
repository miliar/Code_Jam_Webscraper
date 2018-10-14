t = int(raw_input())
cs = []
fs = []
xs = []

for i in xrange(t):
  [c, f, x] = map(float, raw_input().split(' '))
  cs.append(c)
  fs.append(f)
  xs.append(x)

for i in xrange(t):
  c, f, x = cs[i], fs[i], xs[i]
  t = 0
  cookies = 0
  cps = 2

  if x < c:
    print "Case #%d: %.7f" % (i + 1, x / 2)

  else:
    j = 0
    while True:
      if ((x - c) / cps) < (x / (cps + f)):
        break
      cps += f
      j += 1
    t = 0
    for k in xrange(j):
      t += c / (2 + k*f)
    t += x / (2 + j*f)
    print "Case #%d: %.7f" % (i + 1, t)
