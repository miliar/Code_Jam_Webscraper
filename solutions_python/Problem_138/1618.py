def dp(l2, r2):
  global a, b, mp, n
  key = (l2, r2)
  if key in mp: return mp[key]
  n1 = r2 - l2 + 1
  l1 = n - n1
  if not n1:
    mp[key] = 0
    return 0
  mina = a[l1]
  minb, maxb = b[l2], b[r2]
  ret = -1
  if mina > maxb:
    ret  = n1
  if mina < maxb:
    t = dp(l2, r2 - 1)
    ret = max(ret, t)
  if mina > minb:
    t = dp(l2 + 1, r2) + 1
    ret = max(ret, t)
  mp[key] = ret
  return ret

def cal2(a, b, n):
  ret = 0
  for i in xrange(n):
    aa = a[i]
    p1, p2 = -1, -1
    w1, w2 = 2.0, 2.0
    for j in xrange(n):
      bb = b[j]
      if bb == -1: continue
      if bb < aa: # if lose
        if bb < w1:
          w1 = bb
          p1 = j
      if bb > aa: # if win
        if bb < w2:
          w2 = bb
          p2 = j
    if p2 != -1:
      b[p2] = -1
      ret += 1
    elif p1 != -1:
      b[p1] = -1
    else:
      assert 1 == 2

  return n - ret

def solve(tcase):
  global a, b, mp, n
  mp = {}
  n = int(raw_input(''))
  a = sorted([float(x) for x in raw_input('').split()])
  b = sorted([float(x) for x in raw_input('').split()])
  aa = [x for x in a]
  bb = [x for x in b]
  #ans1 = dp(0, n - 1)
  ans1 = n - cal2(bb, aa, n)
  ans2 = cal2(a, b, n)
  print 'Case #%d: %d %d' % (tcase, ans1, ans2)

T = int(raw_input(''))
for tcase in xrange(1, T + 1):
  solve(tcase)