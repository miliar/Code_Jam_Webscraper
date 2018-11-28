def read_matrix():
  a = []
  for i in xrange(4):
    a.append(map(int, raw_input().split()))
  return a

for i in xrange(input()):
  rowb = input()
  before = read_matrix()
  rowa = input()
  after = read_matrix()
  ans = set(before[rowb - 1]).intersection(set(after[rowa - 1]))
  if not ans:
    print "Case #%d: Volunteer cheated!" % (i + 1)
  elif len(ans) > 1:
    print "Case #%d: Bad magician!" % (i + 1)
  else:
    print "Case #%d: %d" % (i + 1, list(ans)[0])

