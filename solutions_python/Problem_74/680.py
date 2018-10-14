import sys

f = open(sys.argv[1],'r')
t = int(f.readline())
for i in xrange(t):
    line = f.readline().split()
    buttons = int(line[0])
    orangeButtons = []
    blueButtons = []
    counter = 0
    for index in range(1,len(line)-1,2):
        if line[index] == 'O':
            orangeButtons.append((counter,int(line[index+1])))
        elif line[index] == 'B':
            blueButtons.append((counter,int(line[index+1])))
        counter += 1
    steps = 0
    counter = 0
    orangePos = 1
    orangeButtonCounter = 0
    bluePos = 1
    blueButtonCounter = 0
    while counter < buttons:
        buttonPushed = False
        if blueButtonCounter == len(blueButtons) or (bluePos == blueButtons[blueButtonCounter][1] and counter != blueButtons[blueButtonCounter][0]):
            pass
        elif bluePos != blueButtons[blueButtonCounter][1]:
            if bluePos < blueButtons[blueButtonCounter][1]:
                bluePos += 1
            elif bluePos > blueButtons[blueButtonCounter][1]:
                bluePos -= 1
        elif bluePos == blueButtons[blueButtonCounter][1] and counter == blueButtons[blueButtonCounter][0]:
            blueButtonCounter += 1
            counter += 1
            buttonPushed = True

        if orangeButtonCounter == len(orangeButtons) or (orangePos == orangeButtons[orangeButtonCounter][1] and counter != orangeButtons[orangeButtonCounter][0]):
            pass
        elif orangePos != orangeButtons[orangeButtonCounter][1]:
            if orangePos < orangeButtons[orangeButtonCounter][1]:
                orangePos += 1
            elif orangePos > orangeButtons[orangeButtonCounter][1]:
                orangePos -= 1
        elif orangePos == orangeButtons[orangeButtonCounter][1] and counter == orangeButtons[orangeButtonCounter][0] and buttonPushed == False:
            orangeButtonCounter += 1
            counter += 1
            buttonPushed = True
        steps += 1

    print "Case #%d: %d" % (i+1, steps)