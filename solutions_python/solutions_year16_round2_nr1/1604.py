import re

inputFile = open ('input.in', 'r')


def main ():
    listL = inputFile.read ().splitlines ()
    stage1 (listL)

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################





    
def stage1 (listL):
    ###############################################################
    ############                                   ################
    ############        Global Variables           ################
    ############                                   ################
    ###############################################################
    output = []
    global CasePointer
    CasePointer = 1 #Change this if second line isn't 1st case
    ###############################################################
    for i in range (1, int(listL[0]) + 1):
        answer = ""
 
        
        ###############################################################
        ###############################################################
        ###############             START            ##################
        ###############################################################
        ###############################################################
        tempS = []
        
        tempS = list(listL[CasePointer])
        print(tempS)
        tempL = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        tempA = []

        j = 0
        while (j < len(tempS)):
            if tempS[j] == "Z":
                tempS.remove("Z")
                tempS.remove("E")
                tempS.remove("R")
                tempS.remove("O")
                j = 0
                tempA.append(0)
            else:
                j = j + 1
        j = 0
        while (j < len(tempS)):
            if tempS[j] == "W":
                tempS.remove("T")
                tempS.remove("W")
                tempS.remove("O")
                tempA.append(2)
                j = 0
            else:
                j = j + 1
        j = 0
        while (j < len(tempS)):
            if tempS[j] == "U":
                tempS.remove("F")
                tempS.remove("U")
                tempS.remove("O")
                tempS.remove("R")
                tempA.append(4)
                j = 0
            else:
                j = j + 1
        j = 0
        while (j < len(tempS)):
            if tempS[j] == "X":
                tempS.remove("S")
                tempS.remove("I")
                tempS.remove("X")
                tempA.append(6)
                j = 0
            else:
                j = j + 1
        j = 0
        while (j < len(tempS)):
            if tempS[j] == "G":
                tempS.remove("H")
                tempS.remove("G")
                tempS.remove("I")
                tempS.remove("E")
                tempS.remove("T")
                tempA.append(8)
                j = 0
            else:
                j = j + 1
  
        j = 0
        while (j < len(tempS)):
            if tempS[j] == "T":
                tempS.remove("H")
                tempS.remove("T")
                tempS.remove("R")
                tempS.remove("E")
                tempS.remove("E")
                tempA.append(3)
                j = 0
            else:
                j = j + 1

        j = 0
        while (j < len(tempS)):
            if tempS[j] == "F":
                tempS.remove("F")
                tempS.remove("I")
                tempS.remove("V")
                tempS.remove("E")
                tempA.append(5)
                j = 0
            else:
                j = j + 1
    

        j = 0
        while (j < len(tempS)):
            if tempS[j] == "S":
                tempS.remove("S")
                tempS.remove("E")
                tempS.remove("V")
                tempS.remove("E")
                tempS.remove("N")
                tempA.append(7)
                j = 0
            else:
                j = j + 1

        j = 0
        while (j < len(tempS)):
            if tempS[j] == "I":
                tempS.remove("N")
                tempS.remove("E")
                tempS.remove("I")                
                tempS.remove("N")
                tempA.append(9)
                j = 0
            else:
                j = j + 1
                
        j = 0
        while (j < len(tempS)):
            if tempS[j] == "O":
                tempS.remove("N")
                tempS.remove("E")
                tempS.remove("O")                                
                tempA.append(1)
                j = 0
            else:
                j = j + 1    
        tempA.sort()
        for j in tempA:
            answer = answer + str(j)
        CasePointer = CasePointer+1
        
        ###############################################################
        ###############################################################
        ###############################################################
        ###############################################################
        ###############################################################
    
        outputLine = "Case #" + str(i) + ": " + answer
        print (outputLine)
        output.append (outputLine)
        printOutput (output)











###############################################################                   
###############################################################
###############################################################
###############################################################
###############################################################
        
def printOutput (output):
    outputFile = open('output', 'w')
    for i in range (0, len (output) - 1):
        outputFile.write (output[i] + "\n")
    outputFile.write (output[len (output) - 1])
            


main()
