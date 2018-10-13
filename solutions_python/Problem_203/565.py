
def setAdjacentOne(j,k, row, column, matrix):
  if k > 0:
    if matrix[j][k-1] != '?':
      matrix[j][k] = matrix[j][k-1]  
      return

  if j > 0:
    if matrix[j-1][k] != '?':
      matrix[j][k] = matrix[j-1][k]
      return

  if k < column - 1:
    if matrix[j][k+1] != '?':
      matrix[j][k] = matrix[j][k+1]
      return

  if j < row - 1:
    if matrix[j+1][k] != '?':
      matrix[j][k] = matrix[j+1][k]
      return

  if k < column - 1:
    setAdjacentOne(j, k+1, row, column, matrix)
    return
  setAdjacentOne(j, k+1, row, column, matrix)   



t = int(raw_input())
for i in xrange(1, t + 1):
  row, column = [int(s) for s in raw_input().split(" ")]
  matrix = []
  for k in xrange(0, row):
    content = raw_input()
    row_content = list(content) #[s for s in content.split(" ")]
    matrix.append(row_content)

  characters = []
  for j in xrange(0, row):
    for k in xrange(0, column):
      if matrix[j][k] != '?':
        characters.append(matrix[j][k])

  for j in xrange(1, row):
    for k in xrange(0, column):
      if matrix[j][k] == '?':
        matrix[j][k] = matrix[j-1][k]

  for j in xrange(row-2, -1, -1):
    for k in xrange(0, column):
      if matrix[j][k] == '?':
        matrix[j][k] = matrix[j+1][k]

  for j in xrange(0, row):
    for k in xrange(1, column):
      if matrix[j][k] == '?':
        matrix[j][k] = matrix[j][k-1]

  for j in xrange(0, row):
    for k in xrange(column-2, -1, -1):
      if matrix[j][k] == '?':
        matrix[j][k] = matrix[j][k+1]

  print "Case #{}:".format(i, matrix)
  for j in xrange(0, row):
    print "{}".format("".join(matrix[j]))


