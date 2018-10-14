br = open('b-large.in')
pw = open('b-large-bs.out', 'w')

f = lambda: int(br.readline())

def solve(c, f, x):
  s, t, o, r = 0, 2, 4, x / 2
  for i in range(400000):
    s += c / t
    t += f
    o -= 1
    r = min(r, s + (x / t))
  return r

n = f()
for t in range(n):
  c, f, x = map(float, br.readline().split())
  pw.write('Case #%d: %.7f\n' % (t + 1, solve(c, f, x)))
  #print('Case #%d: %.7f' % (t + 1, solve(c, f, x)))

