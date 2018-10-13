def main(inputFileName):
  OUTPUT_FILE_LOCATION = r'./Outputs/freeCellStats.out' 
  inputFile = open(inputFileName, 'r')
  outputFile = open(OUTPUT_FILE_LOCATION, 'w')

  numTestCases = inputFile.readline()

  numTestCases = int(numTestCases)  

  for caseNumber in range(1, numTestCases + 1):
    validateFreeCellStats(caseNumber, inputFile, outputFile)

  inputFile.close()
  outputFile.close()

def validateFreeCellStats(caseNumber, inputFile, outputFile):

  freeCellStatsInput = inputFile.readline()

  freeCellStatsListing = freeCellStatsInput.split()

  freeCellStatsListing = [int(statInput) for statInput in freeCellStatsListing]

  gamesTodayUpperBound = freeCellStatsListing[0]
  todaysWinningPercentage = freeCellStatsListing[1]
  allTimeWinningPercentage = freeCellStatsListing[2]

  mayBePossible = True
  
  if allTimeWinningPercentage == 100 and \
      todaysWinningPercentage != 100:
    mayBePossible = False
    possibility = 'Broken'

  if mayBePossible:
    possibleWinsList = []

    for gamesToday in range(1, gamesTodayUpperBound + 1):
      numWinsToday = todaysWinningPercentage * gamesToday / 100

      #Ensure we have a valid number of wins...
      if int(float(numWinsToday)/gamesToday * 100) == todaysWinningPercentage:
        possibleWinsList.append(numWinsToday) 

    if 0 in possibleWinsList and allTimeWinningPercentage == 0 and \
        todaysWinningPercentage == 0:
      possibility = 'Possible'
    elif possibleWinsList and allTimeWinningPercentage > 0:
      possibility = 'Possible'
    else :
      possibility = 'Broken'
     
  caseNumberOutput = 'Case #%s: %s' % (caseNumber, possibility)

  outputFile.write(caseNumberOutput + '\n')

if __name__ == '__main__':
  import sys
  main(sys.argv[1])
