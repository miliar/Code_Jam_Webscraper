Input = open( "C:\Users\josip kotarac\Desktop\A-small-attempt1.in", "r" )
Output = open( "C:\Users\josip kotarac\Desktop\output.txt", "w" )
array = []
chosenRow=0
maxRows = 4
possibleCards=[]
foundCard=0
cardFoundNumber=0
caseNum =0
setDone = False
for line in Input.readlines():
    line = line.split()
    array.append( line )
for index in range(len(array)):

    if (len(array[index])==1):
        chosenRow=int(array[index][0])
        indexInRow = 0
        foundCard = 0
        cardFoundNumber = 0
    elif (len(array[index])==4):
        if (indexInRow==chosenRow-1 and not possibleCards):
            possibleCards=array[index]
        elif (indexInRow==chosenRow-1 and possibleCards):
            caseNum+=1
            for card in array[index]:
                for oldCard in possibleCards:
                    if (card == oldCard):
                        cardFoundNumber+=1
                        foundCard = card
            if (cardFoundNumber>1):
                Output.write( "Case #"+ str(caseNum) +": Bad magician!\n")
            elif (cardFoundNumber==1):
                Output.write( "Case #"+ str(caseNum) +": "+foundCard+"\n")
            elif (cardFoundNumber==0):
                Output.write( "Case #"+ str(caseNum) +": Volunteer cheated!\n")
            possibleCards=[]           
        indexInRow+=1
             
Output.close()
Input.close()