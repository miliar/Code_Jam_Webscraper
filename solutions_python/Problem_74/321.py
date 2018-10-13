def main(inputFileName):
  OUTPUT_FILE_LOCATION = r'./Outputs/BotTrust.out' 
  inputFile = open(inputFileName, 'r')
  outputFile = open(OUTPUT_FILE_LOCATION, 'w')

  numTestCases = inputFile.readline()

  numTestCases = int(numTestCases)  

  for caseNumber in range(1, numTestCases + 1):
    performBotTask(caseNumber, inputFile, outputFile)

  inputFile.close()
  outputFile.close()

def performBotTask(caseNumber, inputFile, outputFile):
  BLUE = 'B'
  ORANGE = 'O'

  botTasksToPerform = inputFile.readline()

  botTasks = botTasksToPerform.split()

  #Drop the First entry which is the number of button presses
  botTasks = botTasks[1:]

  orangeButtonPresses = []
  blueButtonPresses = []
  colorSequence = []

  lastBotSeen = None 

  for task in botTasks:
    if task == ORANGE:
      lastBotSeen = ORANGE
      colorSequence.append(ORANGE)
    elif task == BLUE:
      lastBotSeen = BLUE
      colorSequence.append(BLUE)
    else:
      if lastBotSeen == BLUE:
        blueButtonPresses.append(int(task))
      elif lastBotSeen == ORANGE:
        orangeButtonPresses.append(int(task))

  totalTime = 0 
  orangeBotLocation = 1
  blueBotLocation = 1

  for color in colorSequence:
    if color == ORANGE:
      while orangeButtonPresses and \
          orangeBotLocation != orangeButtonPresses[0]:
        totalTime += 1

        if orangeBotLocation < orangeButtonPresses[0]:
          orangeBotLocation += 1
        else:
          orangeBotLocation -= 1

        if blueButtonPresses and \
            blueBotLocation != blueButtonPresses[0]:
          if blueBotLocation < blueButtonPresses[0]:
            blueBotLocation += 1
          else:
            blueBotLocation -= 1

      #Push Orange's Button
      totalTime += 1
      orangeButtonPresses = orangeButtonPresses[1:]

      #If Blue is still not in position move him in the right direction...
      if blueButtonPresses and \
          blueBotLocation != blueButtonPresses[0]:
        if blueBotLocation < blueButtonPresses[0]:
          blueBotLocation += 1
        else:
          blueBotLocation -= 1

    elif color == BLUE:
      while blueButtonPresses and \
          blueBotLocation != blueButtonPresses[0]:
        totalTime += 1

        if blueBotLocation < blueButtonPresses[0]:
          blueBotLocation += 1
        else:
          blueBotLocation -= 1

        if orangeButtonPresses and \
            orangeBotLocation != orangeButtonPresses[0]:
          if orangeBotLocation < orangeButtonPresses[0]:
            orangeBotLocation += 1
          else:
            orangeBotLocation -= 1

      #Push Blue's Button
      totalTime += 1
      blueButtonPresses = blueButtonPresses[1:]

      #If Orange is still not in position move him in the right direction...
      if orangeButtonPresses and \
          orangeBotLocation != orangeButtonPresses[0]:
        if orangeBotLocation < orangeButtonPresses[0]:
          orangeBotLocation += 1
        else:
          orangeBotLocation -= 1

  caseNumberOutput = 'Case #%s: %s' % (caseNumber, totalTime)

  outputFile.write(caseNumberOutput + '\n')

if __name__ == '__main__':
  import sys
  main(sys.argv[1])
