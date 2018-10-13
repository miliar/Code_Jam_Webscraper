import fileinput

def warBlocks(A, B, deceit):
  score = 0
  for aBlock in A:
    foundBlock = False
    for bBlock in B:
      if bBlock > aBlock:
        foundBlock = True
        B.remove(bBlock)
        break
    if not deceit and not foundBlock:
      score += 1
    elif deceit and foundBlock:
      score += 1
  return score

input = fileinput.input();
testCaseCount = int(input[0])

testCases = []
for x in xrange(0, testCaseCount * 3, 3):
  testCase = {}
  testCase["blockCount"] = int(input[x + 1])
  testCase["naomiBlocks"] = [float(y) for y in input[x + 2].split()]
  testCase["kenBlocks"] = [float(y) for y in input[x + 3].split()]
  testCases.append(testCase)

for i, testCase in enumerate(testCases):
  naomiBlocks = sorted(testCase["naomiBlocks"])
  kenBlocks = sorted(testCase["kenBlocks"])
  dKenBlocks = kenBlocks[:]
  normalScore = 0
  deceitScore = 0

  normalScore = warBlocks(naomiBlocks, kenBlocks, False)
  deceitScore = warBlocks(dKenBlocks, naomiBlocks, True)

  print "Case #" + str(i + 1) + ": " + str(deceitScore) + " " + str(normalScore)