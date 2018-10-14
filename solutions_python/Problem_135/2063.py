ntests = int(raw_input())
for i in xrange(1, ntests+1):
  print "Case #{}:".format(i),

  rowi1 = int(raw_input())
  for j in xrange(rowi1 - 1):
    raw_input()
  row1 = set(map(int, raw_input().split()))
  for j in xrange(4 - rowi1):
    raw_input()
  rowi2 = int(raw_input())
  for j in xrange(rowi2 - 1):
    raw_input()
  row2 = set(map(int, raw_input().split()))
  for j in xrange(4 - rowi2):
    raw_input()

  intx = row1 & row2
  if len(intx) == 0:
    print "Volunteer cheated!"
  elif len(intx) > 1:
    print "Bad magician!"
  else:
    print intx.pop()
