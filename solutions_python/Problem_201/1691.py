def solve(n, k):
  d = {n: 1}
  while k > 0:
    m = max(d.keys())
    smin = (m - 1) / 2
    smax = m / 2
    d[smin] = d.get(smin, 0) + d[m]
    d[smax] = d.get(smax, 0) + d[m]
    k -= d[m]
    del d[m]
  return (smax, smin)

t = int(raw_input())
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  
  sol = solve(n, k)
  print "Case #{}: {} {}".format(i, sol[0], sol[1])

