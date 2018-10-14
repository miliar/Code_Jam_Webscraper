import sys

T = int(sys.stdin.readline())

for ti in range(T):
  r1 = int(sys.stdin.readline())
  for i in range(4):
    l = sys.stdin.readline()
    if i == r1 - 1:
      s1 = {int(x) for x in l.split(' ')}
  r2 = int(sys.stdin.readline())
  for i in range(4):
    l = sys.stdin.readline()
    if i == r2 - 1:
      s2 = {int(x) for x in l.split(' ')}
  su = {x for x in s1 if x in s2}
  if len(su) == 0:
    print "Case #%d: Volunteer cheated!" % (ti + 1)
  elif len(su) > 1:
    print "Case #%d: Bad magician!" % (ti + 1)
  else:
    for x in su:
      print "Case #%d: %d" % (ti + 1, x)
