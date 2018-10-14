t = int(raw_input())
rows1 = []
rows2 = []
boards1 = []
boards2 = []

for i in xrange(t):
  rows1.append(int(raw_input()))
  board1 = []
  for j in xrange(4):
    board1.append(map(int, raw_input().split(' ')))
  boards1.append(board1)
  rows2.append(int(raw_input()))
  board2 = []
  for j in xrange(4):
    board2.append(map(int, raw_input().split(' ')))
  boards2.append(board2)

for i in xrange(t):
  s1 = set(boards1[i][rows1[i] - 1])
  s2 = set(boards2[i][rows2[i] - 1])
  s = s1 & s2
  if len(s) == 1:
    print "Case #%d: %d" % (i + 1, s.pop())
  elif len(s) > 1:
    print "Case #%d: Bad magician!" % (i + 1)
  else:
    print "Case #%d: Volunteer cheated!" % (i + 1)
