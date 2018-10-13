import string

def magicTrick(txtFile):
    infile = open(txtFile, "r")
    testCases = infile.readline()
    testCases = int(testCases)
    
    for i in range(testCases):
        row = int(infile.readline())
        for j in range(row-1):
            infile.readline()
        possibleAns = infile.readline()
        possibleAns = string.split(possibleAns, " ")
        possibleAns[3] = possibleAns[3][:len(possibleAns[3])-1]
        for a in range(4-row):
            infile.readline()
        
        nextRow = int(infile.readline())
        for k in range(nextRow-1):
            infile.readline()
        ansRow = infile.readline()
        ansRow = string.split(ansRow, " ")
        ansRow[3] = ansRow[3][:len(ansRow[3])-1]
        for b in range(4-nextRow):
            infile.readline()
        
        answers = []
        
        for l in range(len(ansRow)):
            if ansRow[l] in possibleAns:
                answers.append(ansRow[l])
        
        if len(answers) == 1:
            print "Case #" + str(i+1) + ": " + str(answers[0])
        elif len(answers) > 1:
            print "Case #" + str(i+1) + ": Bad magician!"
        else:
            print "Case #" + str(i+1) + ": Volunteer cheated!"
        
magicTrick("magicTrickTest.txt")