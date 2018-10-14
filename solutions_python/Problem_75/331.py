def main(inputFileName):
  OUTPUT_FILE_LOCATION = r'./Outputs/magicka.out' 
  inputFile = open(inputFileName, 'r')
  outputFile = open(OUTPUT_FILE_LOCATION, 'w')

  numTestCases = inputFile.readline()

  numTestCases = int(numTestCases)  

  for caseNumber in range(1, numTestCases + 1):
    deriveInvocationList(caseNumber, inputFile, outputFile)

  inputFile.close()
  outputFile.close()

def deriveInvocationList(caseNumber, inputFile, outputFile):
  combosToResultant = {}
  opposerMapping = {}

  invocationCaseString = inputFile.readline()

  invocationCaseListing = invocationCaseString.split()

  numCombiners = int(invocationCaseListing[0])

  if numCombiners > 0:
    combinerListing = invocationCaseListing[1:numCombiners + 1]

    for combination in combinerListing:
      characters = " ".join(combination).split()
      firstBaseElement = characters[0]
      secondBaseElement = characters[1]
      resultantElement = characters[2]

      combo = firstBaseElement + secondBaseElement
      alternateCombo = secondBaseElement + firstBaseElement
      combosToResultant[combo] = resultantElement
      combosToResultant[alternateCombo] = resultantElement
  
  numOpposersIndex = 1
  
  if numCombiners > 0:
    numOpposersIndex += numCombiners

  numOpposers = int(invocationCaseListing[numOpposersIndex])

  if numOpposers > 0:
    firstOpposerIndex = numOpposersIndex + 1
    opposerListing = invocationCaseListing[firstOpposerIndex:firstOpposerIndex + numOpposers]

    for opposers in opposerListing:
      characters = " ".join(opposers).split()
      
      firstOpposer = characters[0]
      secondOpposer = characters[1]

      if firstOpposer in opposerMapping:
        opposerList = opposerMapping[firstOpposer]
        opposerList.append(secondOpposer)
        opposerMapping[firstOpposer] = opposerList
      else :
        opposerMapping[firstOpposer] = [secondOpposer]

      if secondOpposer in opposerMapping:
        opposerList = opposerMapping[secondOpposer]
        opposerList.append(firstOpposer)
        opposerMapping[secondOpposer] = opposerList
      else :
        opposerMapping[secondOpposer] = [firstOpposer]

  finalInvocation = []

  invocationSequence = invocationCaseListing[len(invocationCaseListing) - 1]

  for element in invocationSequence:
    if finalInvocation:
      lastElement = finalInvocation[len(finalInvocation) - 1]
      combo = lastElement + element
      alternateCombo = element + lastElement

      if combo in combosToResultant or \
          alternateCombo in combosToResultant:
            resultantElement = combosToResultant[combo]
            element = resultantElement
            finalInvocation[len(finalInvocation) - 1] = element
      else:
        finalInvocation.append(element)
    else:
      finalInvocation.append(element)

    #Check for Opposers...
    if element in opposerMapping:
      opposers = opposerMapping[element]
    else:
      opposers = []
    
    for testElement in finalInvocation:
      if testElement in opposers:
        finalInvocation = []

  solution = ", ".join(finalInvocation)
  
  if solution:
    solution = '[%s]' % (solution)
  else:
    solution = "[]"

  caseNumberOutput = 'Case #%s: %s' % (caseNumber, solution)

  outputFile.write(caseNumberOutput + '\n')

if __name__ == '__main__':
  import sys
  main(sys.argv[1])
