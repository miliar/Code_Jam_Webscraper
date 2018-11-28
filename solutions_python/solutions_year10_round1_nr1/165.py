f = [l[:-1] for l in file("in2")]
cases  = int(f[0])
f = f[1:]

def rotMatrix(matrix):
    width = len(matrix)

    newMatrix = []

    for x in range(width):
        newMatrix.append([])
        for y in range(width):
            newMatrix[-1] += matrix[width-y-1][x]

    res = []
    for x in newMatrix:
        res.append("".join(x)) 
    return res

def pMatrix(matrix):
    for x in matrix:
        print x

def rightMatrix(matrix):
    width = len(matrix)
    for x in range(width):
        matrix[x] =  matrix[x].replace(".", "")
        matrix[x] = (width-len(matrix[x]))*"." + matrix[x]
    return matrix

def getCol(matrix, which):
    return ''.join([l[which] for l in matrix])


def getDiags(matrix):
    width = len(matrix)
    pair1 = [[x,0] for x in range(width)]
    pair2 = [[0,x] for x in range(width)]
    pair1.extend(pair2)
    ret = []
    for p in pair1:
        newLine = [p]
        newPair = p
        res = ""
        while True:
            res+= matrix[newPair[0]][newPair[1]]
            newPair[0] +=1
            newPair[1] +=1
            if newPair[0] < width and newPair[1] < width:
                continue
            break
        ret.append(res)
    return ret

def getOtherDiags(matrix):
    width = len(matrix)
    pair1 = [[x,0] for x in range(width)]
    pair2 = [[width-1,x] for x in range(width)]
    pair1.extend(pair2)
    ret = []
    for p in pair1:
        newLine = [p]
        newPair = p
        res = ""
        while True:
            res+= matrix[newPair[0]][newPair[1]]
            newPair[0] -=1
            newPair[1] +=1
            if newPair[0] <0 or newPair[0]>=width or newPair[1]<0 or newPair[1] >=width:
                break
            continue
        ret.append(res)
    return ret



def whoWon(matrix, size):
    winners = []
    #horizontal
    width = len(matrix)

    #do testing
    for x in range(width):
        if matrix[x].find("R"*size) != -1:
            winners.append("Red")

        if matrix[x].find("B"*size) != -1:
            winners.append("Blue")

    for x in range(width):
        if getCol(matrix, x).find("R"*size) != -1:
            winners.append("Red")

        if getCol(matrix, x).find("B"*size) != -1:
            winners.append("Blue")

    allDiags = getDiags(matrix)
    allDiags.extend(getOtherDiags(matrix))
    for str in allDiags:
        if str.find("R"*size) != -1:
            winners.append("Red")
        if str.find("B"*size) != -1:
            winners.append("Blue")

    return winners
    

for case in range(cases):
    matrix = []
    height, win = [int(x) for x in f[0].split(" ")]
    f=f[1:]
    for x in range(height):
        matrix.append(f[0])
        f=f[1:]



    rightMatrix(matrix)
    matrix = rotMatrix(matrix)

    winner = whoWon(matrix, win)
    ans = ""
    if len(winner)==0:
        ans = "Neither"
    elif "Red" in winner and not "Blue" in winner:
        ans = "Red"
    elif "Blue" in winner and not "Red" in winner:
        ans = "Blue"
    else:
        ans = "Both"

    print "Case #%d: %s" % ( (case+1), ans)
