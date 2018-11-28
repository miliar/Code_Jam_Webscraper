import string

# _file = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_A/data.txt")
# _file = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_A/A-small-attempt0.in")
_file = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_A/A-large.in")
_result = open("D:/Dropbox/Projects/CodeJAM/2013 Qualification Round/Problem_A/result.txt", "w")

def gameResult(matrix):
  # check for X win (X won)
  _matrix = map(lambda row: map(lambda cell: int(cell == 'X' or cell == 'T'), row), matrix)

  # check for columns and rows
  for i in range(0, 4):
    if sum(_matrix[i]) == 4 or sum(map(lambda row: row[i], _matrix)) == 4:
      return 'X won'

  if sum(map(lambda (row, index): row[index], zip(_matrix, [0,1,2,3]))) == 4:
    return 'X won'
  if sum(map(lambda (row, index): row[index], zip(_matrix, [3,2,1,0]))) == 4:
    return 'X won'

  # check for O win (O won)
  _matrix = map(lambda row: map(lambda cell: int(cell == 'O' or cell == 'T'), row), matrix)

  # check for columns and rows
  for i in range(0, 4):
    if sum(_matrix[i]) == 4 or sum(map(lambda row: row[i], _matrix)) == 4:
      return 'O won'

  if sum(map(lambda (row, index): row[index], zip(_matrix, [0,1,2,3]))) == 4:
    return 'O won'
  if sum(map(lambda (row, index): row[index], zip(_matrix, [3,2,1,0]))) == 4:
    return 'O won'

  # Draw
  _matrix = map(lambda row: map(lambda cell: int(cell == 'O' or cell == 'T' or cell == 'X'), row), matrix)
  if sum(map(lambda row: sum(row), _matrix)) == 16:
    return 'Draw'

  # Game has not completed
  return 'Game has not completed'

matrix = [[0 for x in xrange(4)] for x in xrange(4)]
dataset_size = int(_file.readline())

for i in range(0, dataset_size):
  for j in range(0, 4):
    matrix[j] = list(_file.readline().replace("\n", ""))
  _file.readline() # read last line

  _result.write("Case #" + str(i + 1) + ": " + gameResult(matrix) + "\n")

  # print gameResult(matrix)

_file.close()
_result.close()