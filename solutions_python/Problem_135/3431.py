import sys

cases = int(sys.stdin.readline())
for case in xrange(1, cases + 1):
  opcoes = [] 
  for arrange in xrange(0, 2):
    linha = int(sys.stdin.readline())
    for l in xrange(1, 5):
      the_line = sys.stdin.readline()
      if linha == l:
        opcoes.append([int(i) for i in the_line.split()])

  a = set(opcoes[0])
  a |= set(opcoes[1])

  print "Case #%d:" % case,
  if len(a) == 7:
    for i in xrange(0, 4):
      for j in xrange(0, 4):
        if opcoes[0][i] == opcoes[1][j]:
          print opcoes[0][i]
  elif len(a) == 8:
    print "Volunteer cheated!"
  else:
    print "Bad magician!"
