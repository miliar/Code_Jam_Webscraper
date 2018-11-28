hasDot = False
glen = 4
def testRow(row, value):
    global hasDot
    global glen
    for x in xrange(glen):
        if row[x] != value:
            if row[x] != 'T':
                if row[x] == '.':
                    hasDot = True
                return False
    return True

def testCol(rows, num, value):
    global glen
    for x in xrange(glen):
        if rows[x][num] != value:
            if rows[x][num] != 'T':
                #if row[num][x] == '.':
                #    hasDot = True
                return False
    return True

def testDia1(rows, value):
    global glen
    for x in xrange(glen):
        if rows[x][x] == value or rows[x][x] == 'T':
            pass
        else:
            return False
    return True

def testDia2(rows, value):
    global glen
    for x in xrange(glen):
        if rows[x][3-x] == value or rows[x][3-x] == 'T':
            pass
        else:
            return False
    return True

def testTable(table, value):
    for x in table:
        if testRow(x, value):
            return True
    for x in xrange(len(table)):
        if testCol(table, x, value):
            return True
    if testDia1(table, value) or testDia2(table, value):
        return True
    return False

def testAll(table):
    global hasDot
    hasDot = False
    if testTable(table, 'X'):
        return "X won"
    elif testTable(table, 'O'):
        return "O won"
    elif hasDot == True:
        return "Game has not completed"
    else:
        return "Draw"


def answer():
    fileName = "A-small-attempt0"
    myInput = open(fileName + ".in", "r")
    myOutput = open(fileName + ".out", "w")
    global hasDot
    global glen
    lines = int(myInput.readline()) #number of boards
    for i in xrange(lines):
        table = []
        hasDot = False
        for k in xrange(glen):
            table.append(myInput.readline()[0:glen])
        myOutput.write("Case #"+ str(i+1) +": " + testAll(table) +"\n")
        myInput.readline()

    myInput.close()
    myOutput.close()



import time
start = time.clock()
answer();
end = time.clock() - start
print end, end*150
