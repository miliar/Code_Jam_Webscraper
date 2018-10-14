import sys

iFile = open(sys.argv[1],"r")

size = int(iFile.readline().strip())

for i in range(size):

  row1 = []
  rowNumber1 = int(iFile.readline().strip())
  
  for y in range(4):
    line = iFile.readline().strip().split()
    if y+1 == rowNumber1:
      row1 = [int(x) for x in line]
      
  row2 = []
  rowNumber2 = int(iFile.readline().strip())
  
  for y in range(4):
    line = iFile.readline().strip().split()
    if y+1 == rowNumber2:
      row2 = [int(x) for x in line]
  
  solution = list(set(row1) & set(row2))
  if len(solution) == 0:
    output = "Volunteer cheated!"
  elif len(solution) > 1:
    output = "Bad magician!"
  else:
    output = str(solution[0])
  print("Case #"+str(i+1)+": "+output)
