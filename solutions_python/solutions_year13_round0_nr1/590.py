ctoi = {}
ctoi['.'] = 0
ctoi['X'] = 1
ctoi['O'] = 2
ctoi['T'] = 3

def solve(fIn):
  b = {}

  for i in range(4):
    b[i] = {}
    line = fIn.readline()
    b[i][0] = ctoi[line[0]]
    b[i][1] = ctoi[line[1]]
    b[i][2] = ctoi[line[2]]
    b[i][3] = ctoi[line[3]]

  fIn.readline()

  result = ''  
  # check rows
  all_and = True
  for i in range(4):
    if not(b[i][0] and b[i][1] and b[i][2] and b[i][3]):
      all_and = False
      
    row_and = b[i][0] & b[i][1] & b[i][2] & b[i][3]
    if row_and == ctoi['X']:
      result = 'X won'
      break
    if row_and == ctoi['O']:
      result = 'O won'
      break
    
  # check cols
  if not result:
    for i in range(4):
      col_and = b[0][i] & b[1][i] & b[2][i] & b[3][i]
      if col_and == ctoi['X']:
        result = 'X won'
        break
      if col_and == ctoi['O']:
        result = 'O won'
        break

  # check diag
  if not result:
    diag1 = b[0][0] & b[1][1] & b[2][2] & b[3][3]
    if diag1 == ctoi['X']:
      result = 'X won'
    if diag1 == ctoi['O']:
      result = 'O won'

  if not result:
    diag2 = b[3][0] & b[2][1] & b[1][2] & b[0][3]
    if diag2 == ctoi['X']:
      result = 'X won'
    if diag2 == ctoi['O']:
      result = 'O won'

  if not result:
    if all_and:
      result = 'Draw'
    else:
      result = 'Game has not completed'
    
  return result

def main(filename):
  fIn = open(filename)
  fOut = open(filename+'.out', 'w')
  numTestCases=int(fIn.readline())
  for i in range(numTestCases):
    result = solve(fIn)
    fOut.write('Case #' + str(i+1) + ': ' + str(result) + '\n')

  fIn.close()
  fOut.close()
  return
    

main('D:\\tech\\code_jam\\2013\\Problem A. Tic-Tac-Toe-Tomek\\A-large.in')


