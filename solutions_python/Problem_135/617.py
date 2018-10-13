import fileinput

def intersect(A, B):
  result = []
  for x in A:
      if x in B:
         result.append(x)
  return result

input = fileinput.input();
testCaseCount = int(input[0])

testCases = []
for x in xrange(0, testCaseCount * 10, 10):
  testCase = {}

  testCase["ansOne"] = int(input[x + 1])

  cardsOne = []
  for cardRow in xrange(2, 6):
    for card in input[x + cardRow].split():
      cardsOne.append(int(card))
  testCase["cardsOne"] = cardsOne

  testCase["ansTwo"] = int(input[x + 6])

  cardsTwo = []
  for cardRow in xrange(7, 11):
    for card in input[x + cardRow].split():
      cardsTwo.append(int(card))
  testCase["cardsTwo"] = cardsTwo

  testCases.append(testCase)

for i, testCase in enumerate(testCases):
  ansOne = testCase["ansOne"] - 1
  cardsOne = testCase["cardsOne"]
  ansTwo = testCase["ansTwo"] - 1
  cardsTwo = testCase["cardsTwo"]

  candidates = cardsOne[(ansOne * 4):(ansOne * 4 + 4)]
  candidatesTwo = cardsTwo[(ansTwo * 4):(ansTwo * 4 + 4)]

  result = intersect(candidates, candidatesTwo)
  if len(result) == 1:
    print "Case #" + str(i + 1) + ": " + str(result[0])
  elif len(result) == 0:
    print "Case #" + str(i + 1) + ": Volunteer cheated!"
  else:
    print "Case #" + str(i + 1) + ": Bad magician!"