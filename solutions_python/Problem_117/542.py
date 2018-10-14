
def checkBoard():

  for i in range(N):
    for j in range(M):
      valid = checkSquare(i,j)
      if not valid: return False

  return True

def checkSquare(i,j):

  value = board[i][j]
  rowgood = True
  colgood = True

  # Check row
  for k in range(M):
    if board[i][k] > value:
      rowgood = False
      break

  # Check column
  for l in range(N):
    if board[l][j] > value:
      colgood = False
      break

  return (rowgood or colgood)

# ========================================

f = open("B-small-attempt0.in","r")
numTestCases = int(f.readline())

for testNum in range(numTestCases):
  
  data = f.readline().strip().split()
  N = int(data[0])
  M = int(data[1])

  board = []
  for i in range(N):
    board.append(['']*M)

  # Read test case and load into board
  for i in range(N):
    data = f.readline().strip().split()
    for j in range(M):
      board[i][j] = data[j]

  # Check board and print if pattern is possible
  valid = checkBoard()
  if (valid): print "Case #%i: YES" % (testNum+1)
  else: print "Case #%i: NO" % (testNum+1)

f.close()

