INPUT_FILE = 'magicTrickInput.txt'
OUTPUT_FILE = 'magicTrickOutput.txt'
def magicTrickFunction():
    inputFile = open(INPUT_FILE, 'r')
    outputFile = open(OUTPUT_FILE, 'w')
    noTestCase = int(inputFile.readline())

    for i in xrange(noTestCase):
        outputLine =  "Case #" + str(i+1) + ": "
        theLine = ""
        
        #process first input
        firstInput = int(inputFile.readline())
        possibleCard1 = []
        for j in xrange(firstInput):
            theLine = inputFile.readline()
        count = 0
        card = ''
        while len(possibleCard1) < 4:
            if theLine[count] == " " or theLine[count] == "\n":
                possibleCard1.append(card)
                card = ''
            else:
                card += theLine[count]
            count += 1
        
        #get rid of remaining lines
        for j in xrange(4-firstInput):
            theLine = inputFile.readline()
        
        #process second input
        secondInput = int(inputFile.readline())
        possibleCard2 = []
        for j in xrange(secondInput):
            theLine = inputFile.readline()
        count = 0
        card = ''
        while len(possibleCard2) < 4:
            if theLine[count] == " " or theLine[count] == "\n":
                possibleCard2.append(card)
                card = ''
            else:
                card += theLine[count]
            count += 1
                
        #get rid of remaining lines
        for j in xrange(4-secondInput):
            theLine = inputFile.readline()

        print "list 1: " + str(possibleCard1)
        print "list 2: " + str(possibleCard2)
        #compare 2 possibleCard list
        count = 0
        target = ''
        for card in possibleCard1:
            if card in possibleCard2:
                target = card
                count += 1

        if count == 0:
            outputLine += 'Volunteer cheated!'
        elif count == 1:
            outputLine += target
        else:
            outputLine += 'Bad magician!'
                
        outputFile.write(outputLine + '\n')
            
    inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    magicTrickFunction()