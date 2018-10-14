import numpy

a = numpy.array([[1,2,3],[4,5,6]])
numpy.delete(a,1,0)



def removeMin(board):
  minHeight = numpy.amin(board)
  shape = board.shape
  newBoard = None

  #iterate over rows
  for i in range(shape[0]):
    row = board[i,:]

    isUniform = True
    for element in row:
      if element != minHeight:
        isUniform = False
        break


    if isUniform:
      newBoard = numpy.delete(board, i, 0)
      return newBoard

  #iterate over columns
  for i in range(shape[1]):
    column = board[:,i]

    isUniform = True
    for element in column:
      if element != minHeight:
        isUniform = False
        break

    if isUniform:
      newBoard = numpy.delete(board, i, 1)
      return newBoard

  # No change occured
  return None


def checkDone(board):
  return numpy.amin(board) == numpy.amax(board)



def solve(board):

  if checkDone(board):
    return True
  else:
    newBoard = removeMin(board)

    if newBoard == None:
      return False
    else:
      return solve(newBoard)


#File reading and generating board
f = open('B-large.in')
numCases = int(f.readline())
cases = []

for i in range(numCases):
  dimension = f.readline().split(' ')
  rows = int(dimension[0])
  columns = int(dimension[1])

  board =[]
  for i in range(rows):
    row = f.readline().split(' ')
    row = map(int, row)
    board.append(row)
  
  array = numpy.array(board)
  cases.append(solve(array))


for i, case in enumerate(cases):
  result = "NO"
  if case:
    result = "YES"

  print 'Case #{0}: {1}'.format(i+1, result)





