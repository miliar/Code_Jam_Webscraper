def r_i():
  return map(int, raw_input().split())

def r_f():
  return map(float, raw_input().split())

#def solve(cookies, speed, cost, plus, win):
#  #print (cookies, speed)
#  l = lambda _curr, _speed, _target: (_target - _curr) / _speed
#
#  ans = l(cookies, speed, win)
#  ltr = l(0, speed, cost)
#  if ans > l(0, speed, cost):
#    ans = min(l(0, speed, cost) + solve(cookies, speed + plus, cost, plus, win), ans)
#  return ans


def solve(C, F, X):
  d, t = [], []
  calc_tn = lambda (n): d[n] + X / (2.0 + F * n)
  calc_dn = lambda (n): d[n - 1] + C / (2.0 + F * (n - 1)) if n > 0 else 0

  farms = 0
  while 1:
    d.append(calc_dn(farms))
    t.append(calc_tn(farms))
    if farms > 0 and t[farms] > t[farms - 1]:
      return t[farms - 1]
    farms += 1



(t,) = r_i()
for k in range(1, t + 1):
  (c, f, x) = r_f()
  print "Case #%s: %s" % (k, solve(c, f, x))