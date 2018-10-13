def richardWins(file, case):
  file.write('Case #' + str(case) + ': RICHARD\n')

def richardLoses(file, case):
  file.write('Case #' + str(case) + ': GABRIEL\n')


# hard coding answers because it's late at night and I have to work tomorrow :(
# work's going to be hella fun though, so don't worry about me. :)

readFile = open('D-small-attempt0.in', 'r')
writeFile = open('output-attempt0-0.txt', 'w')

cases = readFile.read().split('\n')
readFile.close()

case = 1
while (case <= int(cases[0])):
  this = cases[case].split()
  omino = int(this[0])
  R = int(this[1])
  C = int(this[2])

  # can't win with one omino
  if (omino == 1):
    richardLoses(writeFile, case)
  if (omino == 2):
    if (R < 2 and C < 2):
      richardWins(writeFile, case)
    # can't be tiled with an odd number of tiles
    elif (R*C % 2 == 1):
      richardWins(writeFile, case)
    else:
      richardLoses(writeFile, case)
  if (omino == 3):
    if ((R < 3 and C < 3) or R < 2 or C < 2):
      richardWins(writeFile, case)
    # 2x4
    elif (R*C == 8):
      richardWins(writeFile, case)
    # 4x4, can't be tiled regardless of shape
    elif (R*C % 3 != 0):
      richardWins(writeFile, case)
    # 3x4, 3x3, 2x3
    else:
      richardLoses(writeFile, case)
  if (omino == 4):
    if ((R < 4 and C < 4) or R < 2 or C < 2):
      richardWins(writeFile, case)
    # can't be tiled with an odd number of tiles
    elif (R*C % 2 == 1):
      richardWins(writeFile, case)
    # 2x4
    elif (R*C == 8):
      richardWins(writeFile, case)
    # 3x4, 4x4
    else:
      richardLoses(writeFile, case)

  case += 1

writeFile.close()
