#!/usr/bin/python


inName = "A-large.in"
outName = "A-large.out"

inFile = open(inName, 'r')
inData = inFile.readlines()
inFile.close()

#print inData

outFile = open(outName, 'wt')

datainBoard = [[],[],[],[]] 

numTest = int(inData[0].replace('\n',''))
data = [[],[],[],[]]
r = 1


def check_row(line):
    isX = 0
    for i in range(4):
        if ( 'X' == line[i] or '.' == line[i]):
            isX = 1 # o is not won
    if (0 == isX):
        return 1 # O is won
    
    isO = 0
    for i in range(4):
        if ( 'O' == line[i] or '.' == line[i] ):
            isO = 1 # x is not won
    if (0 == isO):
        return 2 # X is won
    return 0

def check_col(data):
    line = [[],[],[],[]]
    for i in range(4):
        line[0] = data[0][i]
        line[1] = data[1][i]
        line[2] = data[2][i]
        line[3] = data[3][i]
        #print line
        if(0 != check_row(line)):
            return check_row(line)
    return 0

def check_diagonal1(data):
    line = [[],[],[],[]]
    for i in range(4):
        line[0] = data[0][0]
        line[1] = data[1][1]
        line[2] = data[2][2]
        line[3] = data[3][3]
        return check_row(line)
    
def check_diagonal2(data):
    line = [[],[],[],[]]
    for i in range(4):
        line[0] = data[3][0]
        line[1] = data[2][1]
        line[2] = data[1][2]
        line[3] = data[0][3]
        return check_row(line)

def check_draw(data):
    for i in range(4):
        for j in range(4):
            if ('.' == data[i][j]):
                return 1
    return 0

def check_t4(data):
    for i in range(4):
        if (0 != check_row(data[i])):
            return check_row(data[i])
    if (0 != check_col(data)):
        return check_col(data)
    if (0 != check_diagonal1(data)):
        return check_diagonal1(data)
    if (0 != check_diagonal2(data)):
        return check_diagonal2(data)
    if (1 == check_draw(data)):
        return 3
    
    return 0



for num in range(numTest):
    for i in range(4):
        data[i] =  inData[r]
        r += 1
    #print data[0], data[1], data[2], data[3]
    outFile.write("Case #"+str(num+1)+": ")
    if(1 == check_t4(data)):
        outFile.write("O won")
        print "o won"
    elif(2 == check_t4(data)):
        outFile.write("X won")
        print "x won"
    elif(3 == check_t4(data)):
        outFile.write("Game has not completed")
        print "Game is not completed"
    else:
        outFile.write("Draw")
        print "Draw"
    outFile.write("\n")
    print ''
    r += 1
    













