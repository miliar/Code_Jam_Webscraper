file = open("input.in")
lines = [line.strip() for line in file]
file.close()

numberOfTests = int(lines[0])
currentLine = 1

for testNumber in range(numberOfTests):
    firstAnswer = int(lines[currentLine])
    currentLine += 1
    firstGrid = []
    for i in range(4):
        firstGrid.append(lines[currentLine].split(" "))
        currentLine += 1
    secondAnswer = int(lines[currentLine])
    currentLine += 1
    secondGrid = []
    for j in range(4):
        secondGrid.append(lines[currentLine].split(" "))
        currentLine += 1

    possibleCards = []
    
    possibleCards1 = []
    possibleCards1.extend(firstGrid[firstAnswer-1])
    possibleCards2 = []
    possibleCards2.extend(secondGrid[secondAnswer-1])


    for card in possibleCards1:
        if card in possibleCards2:
            possibleCards.append(card)


    if len(possibleCards) == 1:
        print("Case #"+str(testNumber+1)+": "+possibleCards[0])
    elif len(possibleCards) == 0:
        print("Case #"+str(testNumber+1)+": Volunteer cheated!")
    elif len(possibleCards) > 1:
        print("Case #"+str(testNumber+1)+": Bad magician!")
        
