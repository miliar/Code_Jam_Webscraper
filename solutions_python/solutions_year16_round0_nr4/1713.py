def solve(k, c, s):
  if (k + c - 1) / c > s:
    return "IMPOSSIBLE"
  elif k == 1:
    return 1
  tiles = ""
  groups = [[] for _ in xrange(s)]
  for i in range(k):
    groups[i % s].append(i + 1)
  for i in range(s):
    a, b = 0, 1
    for j in groups[i]:
        a += j * b
        b *= c
    tiles += str(a) + " "
  return tiles

T = input ()
for t in xrange (1, T + 1):
  k, c, s = map(int, raw_input ().split())
  print("Case #%i: %s" % (t, solve(k, c, s)))