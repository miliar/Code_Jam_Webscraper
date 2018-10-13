def get(s):
  for i in s:
    return i

T = int(raw_input())
for t in range(T):
  a = int(raw_input())
  g1 = [map(int, raw_input().split()) for i in range(4)]
  b = int(raw_input())
  g2 = [map(int, raw_input().split()) for i in range(4)]
  s = set(g1[a - 1]).intersection(g2[b - 1])

  print "Case #%d:" % (t + 1),
  if len(s) == 0:
    print "Volunteer cheated!"
  elif len(s) == 1:
    print get(s)
  else:
    print "Bad magician!"
