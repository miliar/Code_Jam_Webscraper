def readInput(f):
    sraw = f.readlines()
    raw = []
    for one in sraw:
        raw.append(one[0:-1])
    noi = int(raw[0])
    out = []
    tmp = 1
    for i in range(noi):
        out.append(raw[tmp:tmp+4])
        tmp+=5
    return noi,out

def judgeLine(line):
    xs = 0
    os = 0
    hasT = False
    for one in line:
        if one == 'X':
            xs += 1
        if one == 'O':
            os += 1
        if one == 'T':
            hasT = True
    if xs == 4 or (xs == 3 and hasT):
        return 'X'
    if os == 4 or (os == 3 and hasT):
        return 'O'
    if (xs + os == 4) or (xs + os == 3 and hasT):
        return 'Draw'
    return 'Not'

def getLines(game):
    lines = []
    for i in range(4):
        lines.append(game[i])
        tmp = ''
        for j in range(4):
            tmp += game[j][i]
        lines.append(tmp)
    tmp = ''
    for i in range(4):
        tmp += game[i][i]
    lines.append(tmp)
    tmp = ''
    for i in range(3, -1, -1):
        tmp += game[i][abs(3-i)]
    lines.append(tmp)
    return lines 

def getResults(data):
    results = []
    for game in data:
        stillDraw = True
        judged = False
        for line in getLines(game):
            if judgeLine(line) == 'X':
                results.append('X won')
                judged = True
                break
            if judgeLine(line) == 'O':
                results.append('O won')
                judged = True
                break
            if judgeLine(line) == 'Draw':
                continue
            if judgeLine(line) == 'Not':
                stillDraw = False
                continue
        if not judged:
            if stillDraw:
                results.append('Draw')
            else:
                results.append('Game has not completed')
    return results
        

f = open('A-large.in')
noi,data = readInput(f)
results = getResults(data)
case = 1
for result in results:
    print 'Case #' + str(case) + ': ' + result
    case += 1

