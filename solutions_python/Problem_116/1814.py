def getboard():
  board = [ raw_input().strip() for _ in xrange(4)]
  return board

def check_win(p,b):
  if check_rows(p,b):
    return True
  if check_cols(p,b):
    return True
  if check_diag(p,b):
    return True
  return False

def match(m,p):
  return m=='T' or m==p

def check_col(p,c,b):
  for r in xrange(4):
    if not match(b[r][c],p):
      return False
  return True

def check_row(p,r,b):
  for c in xrange(4):
    if not match(b[r][c],p):
      return False
  return True

def check_diag(p,b):
  while 1:
    if not match(b[0][0],p): break
    if not match(b[1][1],p): break
    if not match(b[2][2],p): break
    if not match(b[3][3],p): break
    return True
  while 1:
    if not match(b[0][3],p): break
    if not match(b[1][2],p): break
    if not match(b[2][1],p): break
    if not match(b[3][0],p): break
    return True
  return False

def check_rows(p,b):
  for r in xrange(4):
    if check_row(p,r,b):
      return True
  return False

def check_cols(p,b):
  for c in xrange(4):
    if check_col(p,c,b):
      return True
  return False

def board_full(b):
  for c in xrange(4):
    for r in xrange(4):
      if b[r][c] == '.':
        return False
  return True

def main():
  T = int(raw_input())
  for t in xrange(T):
    print 'Case #'+str(t+1)+':',
    b = getboard()
    if t < T-1: raw_input()
    if check_win('X',b):
      print 'X won'
      continue
    if check_win('O',b):
      print 'O won'
      continue
    if board_full(b):
      print 'Draw'
      continue
    print 'Game has not completed'

if __name__=='__main__':
  main()