import sys
inp = sys.stdin.readlines()
num_cases = int(inp[0])
cases = [(i+1, [x.strip() for x in inp[i*5+1:(i+1)*5+1]]) for i in range(num_cases)]
winner = ''
for i, case in cases:
  winner = False
  emptyspace = False
  for line in case:
    if line.count('X') + line.count('T') == 4: winner = 'X'
    if line.count('O') + line.count('T') == 4: winner = 'O'
    if '.' in line: emptyspace = True
  for col in range(4):
    line = ''.join([case[c][col] for c in range(4)])
    if line.count('X') + line.count('T') == 4: winner = 'X'
    if line.count('O') + line.count('T') == 4: winner = 'O'
  line = ''.join([case[diag][diag] for diag in range(4)])
  if line.count('X') + line.count('T') == 4: winner = 'X'
  if line.count('O') + line.count('T') == 4: winner = 'O'
  line = ''.join([case[diag][3-diag] for diag in range(4)])
  if line.count('X') + line.count('T') == 4: winner = 'X'
  if line.count('O') + line.count('T') == 4: winner = 'O'
  
  if winner == False and emptyspace == True: print "Case #%d: Game has not completed" % i
  if winner == False and emptyspace == False: print "Case #%d: Draw" % i
  if winner == 'X': print "Case #%d: X won" % i
  if winner == 'O': print "Case #%d: O won" % i