t = int(raw_input())
for i in xrange(1, t + 1):
  cakes, m = [s for s in raw_input().split(" ")]
  cakes = list(cakes)
  m = int(m)
  s = len(cakes)
  answer = 0
  if m > len(cakes):
    print "Case #{}: IMPOSSIBLE".format(i)
    continue
  if "-" not in cakes:
    print "Case #{}: {}".format(i, answer)
    continue
  for index, cake in enumerate(cakes):
    if cake == "-" and index + m <= s:
      answer = answer + 1
      for x in range(m):
        cakes[index + x] = "+" if cakes[index + x] == "-" else "-"
  if "-" in cakes:
    print "Case #{}: IMPOSSIBLE".format(i)
    continue
  print "Case #{}: {}".format(i, answer)