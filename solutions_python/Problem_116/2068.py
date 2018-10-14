def O_Horizontal():
    boardOH = [[],[],[],[]]
    for i in range(4):
        for j in range(4):

            if j==0 and bigB[i][0] in ('O', 'T'):
                boardOH[i].append(1)
            else:
                boardOH[i].append(0)

    for i in range(4):
        for j in range(1,4):
            if bigB[i][j] in ('O', 'T'):
                boardOH[i][j] = boardOH[i][j-1] +1
                if boardOH[i][j] == 4:
                    return True
    return False
    
def O_Vertical():
    boardOV = [[], [], [], []]
    for i in range(4):
        for j in range(4):

            if i==0 and bigB[0][j] in ('O', 'T'):
                boardOV[i].append(1)
            else:
                boardOV[i].append(0)

    for i in range(1,4):
        for j in range(4):
            if bigB[i][j] in ('O', 'T'):
                boardOV[i][j] = boardOV[i-1][j] +1
                if boardOV[i][j] == 4:
                    return True
    
    return False
    
def O_Diagonal():
    if bigB[0][0] in ('O','T') and bigB[1][1] in ('O','T') and bigB[2][2] in ('O','T') and bigB[3][3] in ('O','T'):
        return True
    elif bigB[0][3] in ('O','T') and bigB[1][2] in ('O','T') and bigB[2][1] in ('O','T') and bigB[3][0] in ('O','T'):
        return True
    else:
        return False

    

def X_Horizontal():
    boardXH = [[],[],[],[]]
    for i in range(4):
        for j in range(4):

            if j==0 and bigB[i][0] in ('X', 'T'):
                boardXH[i].append(1)
            else:
                boardXH[i].append(0)

    for i in range(4):
        for j in range(1,4):
            if bigB[i][j] in ('X', 'T'):
                boardXH[i][j] = boardXH[i][j-1] +1
                if boardXH[i][j] == 4:
                    return True
    return False

    
def X_Vertical():
    boardXV = [[], [], [], []]
    for i in range(4):
        for j in range(4):

            if i==0 and bigB[0][j] in ('X', 'T'):
                boardXV[i].append(1)
            else:
                boardXV[i].append(0)

    for i in range(1,4):
        for j in range(4):
            if bigB[i][j] in ('X', 'T'):
                boardXV[i][j] = boardXV[i-1][j] +1
                if boardXV[i][j] == 4:
                    return True
    return False

    
def X_Diagonal():
    if bigB[0][0] in ('X','T') and bigB[1][1] in ('X','T') and bigB[2][2] in ('X','T') and bigB[3][3] in ('X','T'):
        return True
    elif bigB[0][3] in ('X','T') and bigB[1][2] in ('X','T') and bigB[2][1] in ('X','T') and bigB[3][0] in ('X','T'):
        return True
    else:
        return False



#bigB = [['X','X','X','T'],['.','.','.','.'],['O','O','.','.'],['.','.','.','.']]
bigB = [['.','.','.','.'], ['.','','.','.'], ['.','.','.','.'], ['.','.','.','.']]

def checkWinner():
    if X_Diagonal() or X_Horizontal() or X_Vertical():
        return "X won"
    elif O_Diagonal() or O_Horizontal() or O_Vertical():
        return "O won"
    else:
        for i in bigB:
            if '.' in i:
                return "Game has not completed"
    return "Draw"
        

filename = open("A-large.in","r")
s = filename.readlines()
for i in range(len(s)):
    s[i] = s[i].replace("\n","")
cases = int(s[0])
filename.close()

newFile = open("output.in","w")

start = 1
end = 5
caseN = 1
for i in range(cases):
    newFile.writelines("Case #%s: " %(caseN),)
    a=0
    b=0
    for j in s[start:end]:
        for k in j:
            bigB[a][b] = k
            b+=1
        a+=1
        b=0
    start+=5
    end+=5
    newFile.writelines(checkWinner())
    newFile.writelines("\n")
    caseN+=1
    
newFile.close()     
