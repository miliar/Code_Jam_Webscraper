import fileinput

input = fileinput.input();
testCaseCount = int(input[0])

testCases = []
for x in xrange(1, testCaseCount + 1):
  testCase = {}
  lineList = input[x].split()
  testCase["farmCost"] = float(lineList[0])
  testCase["farmBonus"] = float(lineList[1])
  testCase["cookieRequirement"] = float(lineList[2])
  testCases.append(testCase)

for i, testCase in enumerate(testCases):
  farmCost = testCase["farmCost"]
  farmBonus = testCase["farmBonus"]
  cookieRequirement = testCase["cookieRequirement"]
  currentRate = 2
  totalTime = 0

  while True:
    timeIfUpgradeA = (farmCost / currentRate)
    timeIfUpgradeB = (cookieRequirement / (currentRate + farmBonus))
    timeIfUpgrade = timeIfUpgradeA + timeIfUpgradeB

    timeIfWait = (cookieRequirement / currentRate)
    if (timeIfUpgrade < timeIfWait):
      totalTime += timeIfUpgradeA
      currentRate += farmBonus
    else:
      totalTime += timeIfWait
      break;
  print "Case #" + str(i + 1) + ": " + str(totalTime)