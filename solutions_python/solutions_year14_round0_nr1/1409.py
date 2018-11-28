def r_i():
  return map(int, raw_input().split())


def solve(a1, m1, a2, m2):
  g = [c for c in m1[a1 - 1] if c in m2[a2 - 1]]
  if len(g) == 0:
    return "Volunteer cheated!"
  if len(g) > 1:
    return "Bad magician!"
  return g[0]


(t,) = r_i()
for k in range(1, t + 1):
  ((a1,), m1, (a2,), m2) = (r_i(), [r_i(), r_i(), r_i(), r_i()], r_i(), [r_i(), r_i(), r_i(), r_i()])
  print "Case #%s: %s" % (k, solve(a1, m1, a2, m2))


