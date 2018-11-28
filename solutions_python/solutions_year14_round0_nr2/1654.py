def cal(c, f, x, n):
  global tl
  t = tl[n]
  spd = 2.0 + n * f
  dx = x / spd
  t += dx
  return t

def solve(tcase):
  c, f, x = (float(t) for t in raw_input('').split())
  n = 50010
  
  global tl
  tl = [0.0]
  for i in xrange(1, n):
    dt = tl[-1] + c / (2.0 + (i - 1) * f)
    tl.append(dt)
  
  tim = 99999999999999999999999999999999.0
  for i in xrange(n):
    cnt = cal(c, f, x, i)
    tim = min(tim, cnt)
  
  print 'Case #%d: %.7f' % (tcase, tim)

T = int(raw_input(''))
for tcase in xrange(1, T + 1):
  solve(tcase)