def checkMatrix(matrix):
  hasEmpty = False
  # check rows
  for y in range(4):
    res = checkFour(matrix[y])
    if res < 2:
      return resultToString(res)
    if res == 3:
      hasEmpty = True
      
  # check columns
  for x in range(4):
    res = checkFour([a[x] for a in matrix])
    if res < 2:
      return resultToString(res)
    if res == 3:
      hasEmpty = True
      
  # check diagonals
  res = checkFour([matrix[a][a] for a in range(4)])
  if res < 2:
    return resultToString(res)
  if res == 3:
    hasEmpty = True
      
  res = checkFour([matrix[a][3-a] for a in range(4)])
  if res < 2:
    return resultToString(res)
  if res == 3:
    hasEmpty = True
    
  if hasEmpty:
    return resultToString(3)
  else:
    return resultToString(2)
  

def resultToString(res):
  if res == 0:
    return "X won"
  if res == 1:
    return "O won"
  if res == 2:
    return "Draw"
  if res == 3:
    return "Game has not completed"

def checkFour(fields):
  currentType = ''
  for field in fields:
    if field == '.':
      return 3
      
    if field == 'T':
      continue
      
    if currentType == '':
      currentType = field
      
    if field != currentType:
      return 2
  
  if currentType == 'O':
    return 1
    
  if currentType == 'X':
    return 0
    
iFile = open("A-small-attempt0.in","r")
oFile = open("output.txt","w")

size = int(iFile.readline().strip())

for i in range(size):

  matrix = []
  
  #read input
  for y in range(4):
    line = iFile.readline().strip()
    matrix.append([])
    for x in range(4):
      matrix[y].append(line[x])
  
  iFile.readline()
  
  output = checkMatrix(matrix)
  oFile.write("Case #"+str(i+1)+": "+output+"\n")
