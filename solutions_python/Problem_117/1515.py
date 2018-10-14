def checkMatrix(matrix):
  binaryMap = []
  # check rows
  for row in matrix:
    binaryRow = []
    maxHeight = max(row)
    for field in row:
      if field < maxHeight:
        binaryRow.append(False)
      else:
        binaryRow.append(True)
    binaryMap.append(binaryRow)
  # check columns
  for x in range(len(matrix[0])):
    column = [row[x] for row in matrix]
    maxHeight = max(column)
    for y in range(len(column)):
      if column[y] == maxHeight:
        binaryMap[y][x] = True
  
  # check if there is a False somewhere in the map
  flatMap = [field for row in binaryMap for field in row]
  if False in flatMap:
    return "NO"
  else:
    return "YES"

iFile = open("B-large.in","r")
oFile = open("output.txt","w")

cases = int(iFile.readline().strip())

for i in range(cases):

  matrix = []
  
  size = iFile.readline().strip().split(" ")
  
  N = int(size[0])
  M = int(size[1])
  
  #read input
  for y in range(N):
    line = iFile.readline().strip().split(" ")
    matrix.append([])
    for x in range(M):
      matrix[y].append(int(line[x]))
  
  output = checkMatrix(matrix)
  oFile.write("Case #"+str(i+1)+": "+output+"\n")
