results = []
for t in xrange(input()):
  a1 = input() - 1
  g1 = [[int(x) for x in raw_input().split()] for i in xrange(4)]
  a2 = input() - 1
  g2 = [[int(x) for x in raw_input().split()] for i in xrange(4)]
  intersection = set.intersection(set(g1[a1]), set(g2[a2]))
  if len(intersection) > 1:
    results.append("Case #%d: Bad magician!" % (t+1))
  elif len(intersection) < 1:
    results.append("Case #%d: Volunteer cheated!" % (t+1))
  else:
    results.append("Case #%d: %d" % (t+1, intersection.pop()))
print "\n".join(results)
