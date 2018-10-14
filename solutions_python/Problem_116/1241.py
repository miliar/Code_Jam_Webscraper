from collections import Counter
 
def detect_win(counter):
  if counter['.'] > 0:
    return False
  if counter['T'] + counter['X'] == 4:
    return 'X won'
  if counter['T'] + counter['O'] == 4:
    return 'O won'
  return 1
 
def find_winner(rows):
  complete = True
  for row in rows:
    val = detect_win(Counter(row))
    if not val:
      complete = False
      continue
    if val == 1:
      continue
    return val
 
  for i in xrange(4):
    val = detect_win(Counter(row[i] for row in rows))
    if not val or val == 1:
      continue
    return val

  val = detect_win(Counter(rows[i][i] for i in xrange(4)))
  if val and val != 1:
    return val

  val = detect_win(Counter(rows[i][3-i] for i in xrange(4)))
  if val and val != 1:
    return val

  if complete:
    return 'Draw'
  return 'Game has not completed'

 
cases = int(raw_input())
 
for i in xrange(cases):
  rows = [0]*4
  for x in xrange(4):
    rows[x] = raw_input()
 
  print 'Case #%d:' %(i+1), find_winner(rows)
  raw_input()