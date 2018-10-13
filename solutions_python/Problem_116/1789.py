def testWin(boardL):
    for i in range (4): #Rows
        #print("BOARDL: ",boardL)
        #horizontal checks
        if boardL[i]=="XXXX" or boardL[i]=="TXXX" or boardL[i]=="XTXX" or boardL[i]=="XXTX" or boardL[i]=="XXXT":
            return "X won"
        elif boardL[i]=="OOOO" or boardL[i]=="TOOO" or boardL[i]=="OTOO" or boardL[i]=="OOTO" or boardL[i]=="OOOT":
            return "O won"
        #diagonal checks
        elif (boardL[0][0]=="X" or boardL[0][0]=="T") and (boardL[1][1]=="X" or boardL[1][1]=="T") and (boardL[2][2]=="X" or boardL[2][2]=="T") and (boardL[3][3]=="X" or boardL[3][3]=="T"):
            return "X won"
        elif (boardL[0][0]=="O" or boardL[0][0]=="T") and (boardL[1][1]=="O" or boardL[1][1]=="T") and (boardL[2][2]=="O" or boardL[2][2]=="T") and (boardL[3][3]=="O" or boardL[3][3]=="T"):
            return "O won"
        elif (boardL[3][0]=="X" or boardL[3][0]=="T") and (boardL[2][1]=="X" or boardL[2][1]=="T") and (boardL[1][2]=="X" or boardL[1][2]=="T") and (boardL[0][3]=="X" or boardL[0][3]=="T"):
            return "X won"
        elif (boardL[3][0]=="O" or boardL[3][0]=="T") and (boardL[2][1]=="O" or boardL[2][1]=="T") and (boardL[1][2]=="O" or boardL[1][2]=="T") and (boardL[0][3]=="O" or boardL[0][3]=="T"):
            return "O won"
        else:
            #vertical checks
            for j in range (4):
                if (boardL[0][j]=="X" or boardL[0][j]=="T") and (boardL[1][j]=="X" or boardL[1][j]=="T") and (boardL[2][j]=="X" or boardL[2][j]=="T") and (boardL[3][j]=="X" or boardL[3][j]=="T"):
                    return "X won"
                elif (boardL[0][j]=="O" or boardL[0][j]=="T") and (boardL[1][j]=="O" or boardL[1][j]=="T") and (boardL[2][j]=="O" or boardL[2][j]=="T") and (boardL[3][j]=="O" or boardL[3][j]=="T"):
                    return "O won"
    #Other checks
    for j in range(4):
        for k in range (4):
            if boardL[j][k]==".":
                return "Game has not completed"
    else:
        return "Draw"
    
f = open("A-large.in", "r")
o = open("AOutput.out", "w")
noTestCases = eval(f.readline())
linesL, no, counter, holder = [], 0, 0, []

for lines in f:
    if lines[-1]=="\n" and len(lines)>1:
        holder.append(lines[:-1])
    elif lines=="\n":
        pass
    if len(holder)==4:
        linesL.append(holder)
        holder=[]

for i in range(noTestCases):
    o.write("Case #{0}: {1}\n".format(i+1, testWin(linesL[i])))
    #print("Case #{0}: {1}\n".format(i+1, testWin(linesL[i])), end="")
    #print(linesL[i])
    #print()
