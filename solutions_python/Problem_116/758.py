import string

FILENAME = "A-large.in"
inFile = open(FILENAME, 'r', 0)
fout = open("A_res.in", "w")
line = inFile.readline()
T = int(string.split(line)[0])

def findinrow(aim, L, row):
    return aim in L[row]

def findincolumn(aim, L, column):
    temp = False
    for r in range(4):
        if aim in L[r][column]:
            temp = True
    return temp

def finddiag1(aim,L):
    temp = False
    if aim == L[0][0]:
        temp = True
    if aim == L[1][1]:
        temp = True
    if aim == L[2][2]:
        temp = True
    if aim == L[3][3]:
        temp = True
    return temp

def finddiag2(aim,L):
    temp = False
    if aim == L[0][3]:
        temp = True
    if aim == L[1][2]:
        temp = True
    if aim == L[2][1]:
        temp = True
    if aim == L[3][0]:
        temp = True
    return temp

def win(winner, loser, rubbish, L):
    temp = False
    for r in range(4):
        if findinrow(winner, L, r) == True:
            if findinrow(loser, L, r) == False:
                if findinrow(rubbish, L, r) == False:
                    temp = True
    for c in range(4):
        if findincolumn(winner, L, c) == True:
            if findincolumn(loser, L, c) == False:
                if findincolumn(rubbish, L, c) == False:
                    temp = True
    if finddiag1(winner,L) == True:
        if finddiag1(loser,L) == False:
            if finddiag1(rubbish,L) == False:
                temp = True
    if finddiag2(winner,L) == True:
        if finddiag2(loser,L) == False:
            if finddiag2(rubbish,L) == False:
                temp = True
    return temp


for t in range(T):
    L = []
    for i in range(4):
        line = inFile.readline()
        L.insert(0,line)
    inFile.readline()

    if win('X', 'O', '.', L):
        fout.write ("Case #" + str(t+1) + ": X won\n")
    elif win('O', 'X', '.', L):
        fout.write ("Case #" + str(t+1) + ": O won\n")
    elif win('.', 'a', 'a', L):
        fout.write ("Case #" + str(t+1) + ": Game has not completed\n")
    else:
        fout.write ("Case #" + str(t+1) + ": Draw\n")

fout.close()
