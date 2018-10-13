# OPENS INPUT FILE IN READ MODE, OUTPUT FILE IN WRITE MODE, AND CREATES A LIST FOR LINES OF OUTPUT
inFile = open("C:/Users/Mike's Laptop/Desktop/Code_Jam_2012-Qualifier/A-small-attempt0.in") 
outFile = open("C:/Users/Mike's Laptop/Desktop/Code_Jam_2012-Qualifier/googlese.out", "w") 
outList = []

# READS FIRST LINE, CONVERTS VALUE TO INT N

currentLine = inFile.readline()
N = int(currentLine)


# READS FIRST LINE, CONVERTS VALUES TO INT N & INT M
"""
currentLine = inFile.readline()
currentLineTokens = currentLine.split()
N = int(currentLineTokens[0])
M = int(currentLineTokens[1])
"""


# ITERATES THROUGH N LINES OF INPUT (CASE #(#): output)
"""
curN = 0
while (curN < N):
    curL = 0
    curOutput = ""
    caseNum = curN + 1
    curLine = inFile.readline()

    curOutput = curOutput + "Case #"
    curOutput = curOutput + str(caseNum)
    curOutput = curOutput + ": "
              
    OUTPUT OF EACH ITERATION GOES HERE
    
    curOutput = curOutput + "\n"
    outList.append(curOutput)
    curN = curN + 1
"""

# ITERATES THROUGH N CASES WITH ONE LINE OF INPUT EACH (A) (CASE #(#): output)

curN = 0
while (curN < N):
    curA = 0
    curOutput = ""
    caseNum = curN + 1
    
    curLine = inFile.readline()
    curLineLength = len(curLine)

    curOutput = curOutput + "Case #"
    curOutput = curOutput + str(caseNum)
    curOutput = curOutput + ": "

    x = 0
    while(x < curLineLength):
        curLetter = curLine[x]
        if(curLetter == "a"):
            curOutput = curOutput + "y"
        elif(curLetter == "b"):
            curOutput = curOutput + "h"
        elif(curLetter == "c"):
            curOutput = curOutput + "e"
        elif(curLetter == "d"):
            curOutput = curOutput + "s"
        elif(curLetter == "e"):
            curOutput = curOutput + "o"
        elif(curLetter == "f"):
            curOutput = curOutput + "c"
        elif(curLetter == "g"):
            curOutput = curOutput + "v"
        elif(curLetter == "h"):
            curOutput = curOutput + "x"
        elif(curLetter == "i"):
            curOutput = curOutput + "d"
        elif(curLetter == "j"):
            curOutput = curOutput + "u"
        elif(curLetter == "k"):
            curOutput = curOutput + "i"
        elif(curLetter == "l"):
            curOutput = curOutput + "g"
        elif(curLetter == "m"):
            curOutput = curOutput + "l"
        elif(curLetter == "n"):
            curOutput = curOutput + "b"
        elif(curLetter == "o"):
            curOutput = curOutput + "k"
        elif(curLetter == "p"):
            curOutput = curOutput + "r"
        elif(curLetter == "q"):
            curOutput = curOutput + "z"
        elif(curLetter == "r"):
            curOutput = curOutput + "t"
        elif(curLetter == "s"):
            curOutput = curOutput + "n"
        elif(curLetter == "t"):
            curOutput = curOutput + "w"
        elif(curLetter == "u"):
            curOutput = curOutput + "j"
        elif(curLetter == "v"):
            curOutput = curOutput + "p"
        elif(curLetter == "w"):
            curOutput = curOutput + "f"
        elif(curLetter == "x"):
            curOutput = curOutput + "m"
        elif(curLetter == "y"):
            curOutput = curOutput + "a"
        elif(curLetter == "z"):
            curOutput = curOutput + "q"
        else:
             curOutput = curOutput + curLetter
        x = x + 1
    outList.append(curOutput)
    curN = curN + 1


# ITERATES THROUGH N CASES WITH TWO LINES OF INPUT EACH (A,B) AND TOKENIZES THEM (CASE #(#): output)
"""
curN = 0
while (curN < N):
    curLine = inFile.readline()
    A = curLine.split()
    LenA = len(A)
    curLine = inFile.readline()
    B = curLine.split()
    LenB = len(B)

    curOutput = ""
    caseNum = curN + 1
    curOutput = curOutput + "Case #"
    curOutput = curOutput + str(caseNum)
    curOutput = curOutput + ": "
              
    OUTPUT OF EACH ITERATION GOES HERE
    
    curOutput = curOutput + "\n"
    outList.append(curOutput)
    curN = curN + 1
"""

# ITERATES THROUGH N CASES WITH THREE LINES OF OF INPUT EACH (A,B,C) AND TOKENIZES THEM (CASE #(#): output)
"""
curN = 0
while (curN < N):
    curLine = inFile.readline()
    A = curLine.split()
    LenA = len(A)
    curLine = inFile.readline()
    B = curLine.split()
    LenB = len(B)
    curLine = inFile.readline()
    C = curLine.split()
    LenC = len(C)

    curOutput = ""
    caseNum = curN + 1
    curOutput = curOutput + "Case #"
    curOutput = curOutput + str(caseNum)
    curOutput = curOutput + ": "
              
    OUTPUT OF EACH ITERATION GOES HERE
    
    curOutput = curOutput + "\n"
    outList.append(curOutput)
    curN = curN + 1
"""


# WRITES OUTPUT LINES ALL AT ONCE THEN CLOSES BOTH INPUT AND OUTPUT FILES
outFile.writelines(outList)
inFile.close()
outFile.close()

