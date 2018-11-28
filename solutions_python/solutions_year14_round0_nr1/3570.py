t = input()

for case in xrange(1, t+1):
  row1 = input()

  firstCards = set()
  for i in xrange(0, 4):
    col = raw_input()
    col = col.split(' ')

    if row1 == i+1:
      firstCards.add(col[0])
      firstCards.add(col[1])
      firstCards.add(col[2])
      firstCards.add(col[3])

  row2 = input()

  secondCards = set()
  for i in xrange(0, 4):
    col = raw_input()
    col = col.split(' ')

    if row2 == i+1:
      secondCards.add(col[0])
      secondCards.add(col[1])
      secondCards.add(col[2])
      secondCards.add(col[3])

  intersection = firstCards.intersection(secondCards)

  if len(intersection) == 0:
    intersection = 'Volunteer cheated!'
  elif len(intersection) == 1:
    intersection = intersection.pop()
  elif len(intersection) >= 2:
    intersection = 'Bad magician!'

  print 'Case #%d: %s' % (case, intersection)
