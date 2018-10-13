def main(inputFileName):
  OUTPUT_FILE_LOCATION = r'./Outputs/candySplitting.out' 
  inputFile = open(inputFileName, 'r')
  outputFile = open(OUTPUT_FILE_LOCATION, 'w')

  numTestCases = inputFile.readline()

  numTestCases = int(numTestCases)  

  for caseNumber in range(1, numTestCases + 1):
    maximizeSeansCandy(caseNumber, inputFile, outputFile)

  inputFile.close()
  outputFile.close()

def maximizeSeansCandy(caseNumber, inputFile, outputFile):
  numCandies = int(inputFile.readline())

  candyValueString = inputFile.readline()
  candyValueListing = [int(value) for value in candyValueString.split()]

  candyValueListing = sorted(candyValueListing)

  patricksPile = candyValueListing[0:1]
  seansPile = candyValueListing[1:]
  
  patricksPerceivedSelfValue = getPatricksPerceivedValue(patricksPile)
  patricksPerceivedSeanValue = getPatricksPerceivedValue(seansPile)

  while patricksPerceivedSelfValue != patricksPerceivedSeanValue:
    seansLowestCandy = seansPile.pop(0)
    patricksPile.append(seansLowestCandy)

    if not patricksPile or not seansPile:
      break

    patricksPerceivedSelfValue = getPatricksPerceivedValue(patricksPile)
    patricksPerceivedSeanValue = getPatricksPerceivedValue(seansPile)

  if not patricksPile or \
      not seansPile:
       maxValue = 'NO'
  else:
    maxValue = sum(seansPile)
  
  caseNumberOutput = 'Case #%s: %s' % (caseNumber, maxValue)

  outputFile.write(caseNumberOutput + '\n')

def getPatricksPerceivedValue(candyValues):
  return reduce(lambda x,y : x^y, candyValues)

if __name__ == '__main__':
  import sys
  main(sys.argv[1])
