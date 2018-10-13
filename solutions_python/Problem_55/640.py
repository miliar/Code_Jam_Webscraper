def runRide(R, k, g):
  g_i = 0
  revenue = 0
  for i in range(0, R):
    riders = 0
    g_i0 = g_i
    while (riders + g[g_i] <= k):
      riders += g[g_i]
      g_i = (g_i + 1) % len(g)
      if (g_i == g_i0): break
    revenue += riders

  return revenue

T = input()
for i in range(1, T + 1):
  (R, k, N) = map(int, raw_input().split(' '))
  g = (map(int, raw_input().split(' ')))
  rev = runRide(R, k, g)
  print "Case #%s: %s" % (i, rev)



