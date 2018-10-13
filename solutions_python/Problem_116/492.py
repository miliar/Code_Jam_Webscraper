def won():
  for i in range(4):
    if p != c(i) != 'T': return False
  return True
check =\
  [lambda j: b[j][j], lambda j: b[3-j][j]] +\
  [lambda j, r = r: b[r][j] for r in range(4)] +\
  [lambda j, c = c: b[j][c] for c in range(4)]
for i in range(1, input()+1):
  b = [raw_input() for j in range(4)]
  w = 0
  for p in 'X', 'O':
    for c in check:
      if won(): w = p
  print 'Case #%i:'%i,
  if w: print w, 'won'
  elif '.' not in b[0]+b[1]+b[2]+b[3]: print 'Draw'
  else: print 'Game has not completed'
  raw_input()
