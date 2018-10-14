def line(f):
  return f.readline().strip()

f = open("A-small-attempt0.in", "r")
o = open("1.out", "w")

T = int(line(f))

for t in xrange(T):
  ans1 = int(line(f))
  arr1 = []
  for i in xrange(4):
    arr1.append(map(int, line(f).split()))
  ans2 = int(line(f))
  arr2 = []
  for i in xrange(4):
    arr2.append(map(int, line(f).split()))
  overlap = set(arr1[ans1-1]).intersection(set(arr2[ans2-1]))
  if len(overlap) == 0:
    s = "Case #%d: Volunteer cheated!" % (t+1)
  elif len(overlap) == 1:
    s = "Case #%d: %d" % (t+1, overlap.pop())
  else:
    s = "Case #%d: Bad magician!" % (t+1)
  print>>o, s
