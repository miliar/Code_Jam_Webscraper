t = int(raw_input())
for i in range(t):
  rows = []
  for j in range(4): rows.append(raw_input())
  state = 0
  for j in range(4):
    if reduce(lambda x,y:x and y in ['T','O'], rows[j], True): state = state or 'O'
    if reduce(lambda x,y:x and y in ['T','X'], rows[j], True): state = state or 'X'
    if reduce(lambda x,y:x and y in ['T','O'], [x[j] for x in rows], True): state = state or 'O'
    if reduce(lambda x,y:x and y in ['T','X'], [x[j] for x in rows], True): state = state or 'X'
  if reduce(lambda x,y:x and y in ['T','X'], [x[e] for e,x in enumerate(rows)], True): state = state or 'X'
  if reduce(lambda x,y:x and y in ['T','O'], [x[e] for e,x in enumerate(rows)], True): state = state or 'O'
  if reduce(lambda x,y:x and y in ['T','X'], [x[3-e] for e,x in enumerate(rows)], True): state = state or 'X'
  if reduce(lambda x,y:x and y in ['T','O'], [x[3-e] for e,x in enumerate(rows)], True): state = state or 'O'
  full = sum([sum([1 if x in ['X','O','T'] else 0 for x in r]) for r in rows])
  if state: print "Case #%d: %s won" % (i+1,state)
  elif full == 16: print "Case #%d: Draw" % (i+1)
  else: print "Case #%d: Game has not completed" % (i+1)
  raw_input()
