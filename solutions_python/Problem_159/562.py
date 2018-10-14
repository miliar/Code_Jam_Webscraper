readFile = open('A-large.in', 'r')
writeFile = open('monster_output_large.txt', 'w')

cases = readFile.readlines() #.split('\n')
readFile.close()

case = 1
while (case <= int(cases[0])):
  mushrooms = cases[case * 2].strip().split()

  i = 0
  greatestDiff = int(mushrooms[0]) - int(mushrooms[1])
  totalEaten = 0
  while i < len(mushrooms) - 1:
    curDiff = int(mushrooms[i]) - int(mushrooms[i + 1])
    if (curDiff > 0):
      totalEaten += curDiff
    if (curDiff > greatestDiff):
      greatestDiff = curDiff
    i += 1

  i = 0
  restEaten = 0
  while i < len(mushrooms) - 1:
    current = int(mushrooms[i])
    if (current < greatestDiff):
      restEaten += current
    else:
      restEaten += greatestDiff
    i += 1

  writeFile.write('Case #' + str(case) + ': ' + str(totalEaten) + ' ' + str(restEaten) + '\n')
  case += 1

writeFile.close()


