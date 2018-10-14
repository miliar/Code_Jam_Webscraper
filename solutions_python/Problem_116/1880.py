dataset = open("input.txt","r")
outfile = open("output.txt","w")
outputset = ""
status = False



CaseNumber = 1
def manageBoard():
  ##Tomek Inbound False Checks

  ## Check for row wins first
  for row in board:
    if row.count('O') == 4 or (row.count('O') == 3 and row.count('T') == 1):
        return 'o'
    elif row.count('X') == 4 or (row.count('X') == 3 and row.count('T') == 1):
        return 'x'

  ##Now for coulumn wins
  for row in vert:
    if row.count('O') == 4 or (row.count('O') == 3 and row.count('T') == 1):
        return 'o'
    elif row.count('X') == 4 or (row.count('X') == 3 and row.count('T') == 1):
        return 'x'

  diag1 = [board[0][0],board[1][1],board[2][2],board[3][3]]
  diag2 = [board[0][3],board[1][2],board[2][1],board[3][0]]
  if diag1.count('O') == 4 or (diag1.count('O') == 3 and diag1.count('T') == 1):
        return 'o'
  elif diag1.count('X') == 4 or (diag1.count('X') == 3 and diag1.count('T') == 1):
        return 'x'
  if diag2.count('O') == 4 or (diag2.count('O') == 3 and diag2.count('T') == 1):
        return 'o'
  elif diag2.count('X') == 4 or (diag2.count('X') == 3 and diag2.count('T') == 1):
        return 'x'
  ##Now for draws n shiz
  dotcount = 0
  for row in board:
    dotcount += row.count('.')
  if dotcount == 0:
    return 'd'
  else:
    return 'n'

T = int(dataset.readline())
for case in xrange(T):
    row1 = list(dataset.readline().rstrip('\n'))
    row2 = list(dataset.readline().rstrip('\n'))
    row3 = list(dataset.readline().rstrip('\n'))
    row4 = list(dataset.readline().rstrip('\n'))
    board = []
    board.append(row1)
    board.append(row2)
    board.append(row3)
    board.append(row4)
    vert = zip(*board[::-1])
    emptyline = dataset.readline()
    if manageBoard() == "x":
        outputset = outputset + "Case #"+str(CaseNumber)+":"+ " X won\n"
        CaseNumber += 1
    elif manageBoard() == "o":
        outputset = outputset + "Case #"+str(CaseNumber)+":"+ " O won\n"
        CaseNumber += 1
    elif manageBoard() == "n":
        outputset = outputset + "Case #"+str(CaseNumber)+":" + " Game has not completed\n"
        CaseNumber += 1
    elif manageBoard() == "d":
        outputset = outputset + "Case #"+str(CaseNumber)+":" + " Draw\n"
        CaseNumber += 1
print(outputset)
outfile.write(outputset)
outfile.close()


