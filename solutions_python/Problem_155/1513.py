readFile = open('A-large.in', 'r')
writeFile = open('standing_output3.txt', 'w')

cases = readFile.readlines() #.split('\n')
readFile.close()

case = 1
while (case <= int(cases[0])):
  show = cases[case].strip().split()

  totalStanding = 0
  bribes = 0
  shyness = 0
  while (shyness <= int(show[0])):
    if (shyness - totalStanding > 0):
      bribes += shyness - totalStanding
      totalStanding += shyness - totalStanding
    totalStanding += int(show[1][shyness])
    shyness += 1

  writeFile.write('Case #' + str(case) + ': ' + str(bribes) + '\n')
  case += 1

writeFile.close()
