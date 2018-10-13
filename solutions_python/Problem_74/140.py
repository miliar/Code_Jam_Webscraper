"""
    Code Jam 2011 Qualification Round, Problem A

    gaz@bitplane.net

"""

with open('input.txt') as inputFile:
    testCount = int(inputFile.readline())
    
    for testNumber in range(testCount):
        testData  = inputFile.readline()[:-1].split(' ')[1:]

        Robots = {'O': {'T':0, 'P':1},
                  'B': {'T':0, 'P':1},
                  'X': {'T':0, 'P':1}} # X is no bot
        LastButtonPress = 0
        LastBotID = 'X'

        for instruction in [(testData[i], testData[i+1]) for i in range(0, len(testData), 2)]:
            # wait for the last robot to press the button
            LastButtonPress = Robots[LastBotID]['T']

            # select the current bot
            LastBotID = instruction[0]
            CurrentBot = Robots[LastBotID]
            newPos = int(instruction[1])
            
            # Give the bot instructions to move
            movementTime    = CurrentBot['T'] + abs(newPos - CurrentBot['P'])
            
            buttonPressTime = max(movementTime + 1, LastButtonPress + 1)
            CurrentBot['T'] = buttonPressTime
            CurrentBot['P'] = newPos

        LastButtonPress = Robots[LastBotID]['T']
        print("Case #{number}: {time}".format(number=testNumber+1, time=LastButtonPress))
