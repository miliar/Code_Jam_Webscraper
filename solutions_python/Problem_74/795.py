def find(function,list):
    for itemIndex in range(0,len(list)):
        if function(list[itemIndex]):
            return itemIndex


file = open("C:\CodeJam\\QualificationALarge.in","r")
output = open("C:\CodeJam\\QualificationALarge.txt","w")

cases = int(file.readline())

for case in range(1,cases+1):
    caseText = file.readline()
    totalMoves = caseText[0]
    movedRobot = []
    moveLocation = []

    for character in caseText.strip().split(" ")[1:]:
        if character.isnumeric():
            moveLocation.append(int(character))
        else:
            movedRobot.append(character)

    bLocation = 1
    oLocation = 1
    movesMade = 0
    for move in range(0,len(movedRobot)):
        moveDone = False
        while not moveDone:

            #bluemove
            if "B" in movedRobot[move:]:
                bDestination = moveLocation[move:][find(lambda robot:robot=="B",movedRobot[move:])]
                if bDestination > bLocation:
                    bLocation += 1
                elif bDestination < bLocation:
                    bLocation -= 1
                elif bDestination == bLocation:
                    if movedRobot[move] == "B":
                        moveDone = True

            #orangemove
            if "O" in movedRobot[move:]:
                oDestination = moveLocation[move:][find(lambda robot:robot=="O",movedRobot[move:])]
                if oDestination > oLocation:
                    oLocation += 1
                elif oDestination < oLocation:
                    oLocation -= 1
                elif oDestination == oLocation:
                    if movedRobot[move] == "O":
                        moveDone = True
            movesMade += 1

    output.write("Case #"+str(case)+": "+str(movesMade))
    if case != cases:
        output.write("\n")

output.close()