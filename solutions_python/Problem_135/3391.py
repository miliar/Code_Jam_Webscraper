import sys
finput = open(sys.argv[1], 'r')
foutput = open(sys.argv[2], 'w')
  
tests = finput.readline()
for test in range(int(tests)):
  guess1 = finput.readline()
  grid1 = []
  answer = 0
  numanswers = 0
  for i in range(4):
    grid1.append(finput.readline().split(' '))

  guess2 = finput.readline()
  grid2 = []
  for i in range(4):
    grid2.append(finput.readline().split(' '))

  for card1 in range(len(grid1[int(guess1) - 1])):
    #print card1
    for card2 in range(len(grid2[int(guess2) - 1])):
      if int(grid1[int(guess1) - 1][card1]) == int(grid2[int(guess2) - 1][card2]):
        answer = int(grid1[int(guess1) - 1][card1])
        numanswers += 1
      
  case = test + 1
  if numanswers == 0:    
    foutput.write("Case #%s: Volunteer cheated!" % case)
    foutput.write("\n")
  elif numanswers == 1:
    foutput.write("Case #%s: %s" % (case, answer))
    foutput.write("\n")
  else:
    foutput.write("Case #%s: Bad magician!" % case)
    foutput.write("\n")