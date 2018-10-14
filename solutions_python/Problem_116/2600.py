import sys



print sys.argv

myFile = open(sys.argv[1],'r')
linesIn = myFile.readlines()
myFile.close()

#First lines
nbCases = int(linesIn[0])
print("There will be " + str(nbCases) + " games")
linesIn = linesIn[1:len(linesIn)]
diag2 = [(0,3), (1,2), (2,1), (3,0)]

def readBoard(lines):
    i = 0
    cols = {"X" : [0, 0, 0, 0], "O" : [0, 0, 0, 0] }
    lins = {"X" : [0, 0, 0, 0], "O" : [0, 0, 0, 0] }
    diags = {"X" : [0, 0], "O" : [0, 0] }
    notFinished = False
    for line in lines:
        for j in range(0,4):
            player = line[j]
            if player == ".":
                notFinished = True
                continue
            if player == "T":
                cols["X"][j] = cols["X"][j] + 1
                cols["O"][j] = cols["O"][j] + 1
                lins["X"][i] = lins["X"][i] + 1
                lins["O"][i] = lins["O"][i] + 1
            else:
                lins[player][i] = lins[player][i] + 1
                cols[player][j] = cols[player][j] + 1
            if i == j: #diag1
                if player == "T":
                    diags["O"][0] = diags["O"][0] + 1
                    diags["X"][0] = diags["X"][0] + 1
                else:
                    diags[player][0] = diags[player][0] + 1
            elif (i,j) in diag2:
                if player == "T":
                    diags["O"][1] = diags["O"][1] + 1
                    diags["X"][1] = diags["X"][1] + 1
                else:
                    diags[player][1] = diags[player][1] + 1
        i = i + 1
    for i in range(0,4):
        for letter in ["X", "O"]: 
            if (cols[letter][i] == 4 or lins[letter][i] == 4 or diags[letter][0] == 4 or diags[letter][1] == 4):
                return letter + " won"
            
    if notFinished: return "Game has not completed"
    else: return "Draw"
    
lines = []
for i in range(0, nbCases):
    #print "".join(linesIn[0:4])
    #print(readBoard(linesIn[0:4]))
    string = readBoard(linesIn[0:4])

    lines.append("Case #" + str(i+1) + ": " + string+ "\n")
    linesIn = linesIn[5:len(linesIn)]

myFile = open(sys.argv[2],'w')
myFile.writelines(lines)
myFile.close()
print "".join(lines)