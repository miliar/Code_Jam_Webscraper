import sys
T = int(sys.stdin.readline())
for t in range(T):
  card1 = int(sys.stdin.readline())
  lines = []
  for i in range(4):
    lines.append(sys.stdin.readline())
  cards = map(int,lines[card1-1].split())

  card1 = int(sys.stdin.readline())
  lines = []
  for i in range(4):
    lines.append(sys.stdin.readline())
  cards2 = map(int,lines[card1-1].split())
  sel = set(cards) & set(cards2)
  print 'Case #' + str(t+1) + ':',
  if len(sel) == 1:
    print list(sel)[0]
  elif len(sel) > 1:
    print 'Bad magician!'
  else:
    print 'Volunteer cheated!'