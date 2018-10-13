# Google Code Jam: Qualifying Round - Magic Trick

fileHandle = open ( 'A-small-attempt0.in', 'r' )
data_list = fileHandle.readlines()
fileHandle.close()

data = iter(data_list)
numCases = int(data.next())

for caseNumber in range(1, numCases + 1):
  
  firstAnswer = data.next()

  firstGrid = [
      data.next().split(),
      data.next().split(),
      data.next().split(),
      data.next().split()
  ]

  firstPossibleCards = firstGrid[int(firstAnswer) - 1]
  
  secondAnswer = data.next()

  secondGrid = [
      data.next().split(),
      data.next().split(),
      data.next().split(),
      data.next().split()
  ]

  secondPossibleCards = secondGrid[int(secondAnswer) - 1]

  count = 0
  correctCard = 0
  for value in firstPossibleCards:
    
    if value in secondPossibleCards:
      count = count + 1
      correctCard = value

  output = "Case #" + str(caseNumber) + ": "
  if count == 0:
    output = output + "Volunteer cheated!"
  elif count > 1:
    output = output + "Bad magician!"
  else:
    output = output + str(correctCard)

  print output
