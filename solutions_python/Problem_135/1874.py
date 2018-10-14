testNumbers = 0
with open ('A-small-attempt0.in') as testFile:
  testNumbers = int(testFile.readline())
  #print "number of test: %d" % testNumbers
  for i in range(0, testNumbers):
    firstGuessRow = testFile.readline()
    #print "first guess" + firstGuessRow
    firstLayout = []
    for j in range(0, 4):
      firstLayout.append(testFile.readline().split())
    #print firstLayout
    secondGuessRow = testFile.readline()
    #print "second guess" + secondGuessRow
    secondLayout = []
    for j in range(0, 4):
      secondLayout.append(testFile.readline().split())
    #print secondLayout

    firstGuessRow =  int(firstGuessRow)
    secondGuessRow = int(secondGuessRow)
    # the same element is 0
    same = 0
    founndElement = 0
    for element in firstLayout[firstGuessRow-1]:
      for element2 in secondLayout[secondGuessRow-1]:
        if element == element2:
          same += 1
          foundElement = int(element)
    if same == 1:
      print "Case #%d: %d" % (i+1, foundElement)
    elif same > 1:
      print "Case #%d: Bad magician!" % (i+1)
    else:
      print "Case #%d: Volunteer cheated!" %(i+1)



