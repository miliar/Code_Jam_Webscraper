for cases in xrange(int(raw_input())):
  first = int(raw_input())
  board = [[int(x) for x in raw_input().split()] for y in xrange(4)]
  possibles = set(board[first-1])
  second = int(raw_input())
  board = [[int(x) for x in raw_input().split()] for y in xrange(4)]
  otherPossibles = set(board[second-1])

  answer = possibles.intersection(otherPossibles)
  if len(answer) == 0:
    out = 'Volunteer cheated!'
  elif len(answer) == 1:
    out = str(answer.pop())
  else:
    out = 'Bad magician!'
  print 'Case #%d: %s' % (cases+1, out)
