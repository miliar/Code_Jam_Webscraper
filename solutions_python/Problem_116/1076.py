def check(s):
  if s == 104 or s == 128:
    return 1
  elif s == 4 or s == 11:
    return 2
  else:
    return 0


d = {'X': 32, 'O': 1, '.': 0, 'T': 8}
NNN = int(raw_input())
for nnn in xrange(1, NNN+1):
  print "Case #%d:" % (nnn),
  state = 0
  B = [[d[x] for x in raw_input()] for i in xrange(4)]
  raw_input()

  if state == 0:
    for x in B:
      state = check(sum(x))
      if state: break

  if state == 0:
    for i in xrange(4):
      state = check(sum([x[i] for x in B]))
      if state: break

  if state == 0:
    state = check(sum([B[i][i] for i in xrange(4)]))

  if state == 0:
    state = check(sum([B[3-i][i] for i in xrange(4)]))

  if state == 0:
    for x in B:
      if 0 in x:
        state = 3
        break

  if state == 1:
    print "X won"
  elif state == 2:
    print "O won"
  elif state == 3:
    print "Game has not completed"
  else:
    print "Draw"
