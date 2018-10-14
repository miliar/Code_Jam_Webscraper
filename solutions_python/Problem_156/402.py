mp = None

def dp(v):
  global mp
  if v in mp:
    return mp[v]
  # print v
  if max(v) == 1:
    return 1
  t1 = tuple([t - 1 for t in v if t > 1])
  ans = dp(t1)
  t2 = list(v)
  mx = t2.pop(-1)
  for i in xrange(1, mx):
    t3 = sorted(t2[:] + [i] + [mx-i])
    ans = min(ans, dp(tuple(t3)))
  ans += 1
  mp[v] = ans
  return ans

def getcnt(x, p):
  if x <= 0:
    return 0
  return (x - 1) / p + 1

def getans(v):
  Min = 2 ** 60
  for i in xrange(1, max(v) + 1):
    cnt = sum(getcnt(x - i, i) for x in v)
    cnt += i
    Min = min(Min, cnt)
  return Min

def solve(tcase):
  global mp
  mp = {}
  d = int(raw_input(''))
  p = raw_input('').split()
  p = [int(t) for t in p]
  p = sorted(p)
  
  #a1 = dp(tuple(p))
  a2 = getans(p)
  #assert a1 == a2
  print 'Case #%d: %s' % (tcase, a2)

T = int(raw_input(''))
for tcase in xrange(1, T + 1):
  solve(tcase)