inputFile = open('D-small-attempt3.in', 'r')

outputFile = open('output', 'w')


nbTests = int(inputFile.readline())

for i in range(nbTests):
  x, r, c = inputFile.readline().split()
  x = int(x)
  r = int(r)
  c = int(c)
  possible = False

  if x == 4:
    if r + c >= 7:
      possible = True

  elif x == 3:
    if (r*c) % 3 == 0 and c > 1 and r > 1:
      possible = True

  elif x == 2:
    if (r*c) % 2 == 0:
      possible = True

  elif x == 1:
    possible = True


  winner = "RICHARD"
  if possible:
    winner = "GABRIEL"
  outputFile.write("Case #" + str(i + 1) + ": " + winner + "\n")



