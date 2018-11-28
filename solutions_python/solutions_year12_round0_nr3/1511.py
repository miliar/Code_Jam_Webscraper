# OPENS INPUT FILE IN READ MODE, OUTPUT FILE IN WRITE MODE, AND CREATES A LIST FOR LINES OF OUTPUT
inFile = open("C:/Users/Mike's Laptop/Desktop/Code_Jam_2012-Qualifier/C-small-attempt0.in") 
outFile = open("C:/Users/Mike's Laptop/Desktop/Code_Jam_2012-Qualifier/recycle.out", "w") 
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
    matches = 0
    curA = 0
    curOutput = ""
    caseNum = curN + 1
    
    curLine = inFile.readline()
    A = curLine.split()

    lowerBound = int(A[0])
    upperBound = int(A[1])
    numLength = len(str(lowerBound))

    curOutput = curOutput + "Case #"
    curOutput = curOutput + str(caseNum)
    curOutput = curOutput + ": "

    print lowerBound
    curLow = lowerBound
    while(curLow != upperBound):
        curHigh = curLow + 1
        curLowString = str(curLow)
        while(curHigh != upperBound + 1):
            x = 0
            curHighString = str(curHigh)
            while(x < numLength):
                tempHighString = curHighString
                curHighString = tempHighString[len(tempHighString)-1] + tempHighString[:len(tempHighString)-1]

                if(int(curHighString) == int(curLowString)):
                    matches = matches + 1
                    break
                
                x = x+1

            curHigh = curHigh + 1
        curLow = curLow + 1
    curOutput = curOutput + str(matches)
    curOutput = curOutput + "\n"
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

