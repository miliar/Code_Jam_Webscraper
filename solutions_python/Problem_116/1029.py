def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def check(rows, pos):
    xWon = True
    oWon = True
    for i in pos:
        a = rows[i[0]][i[1]]
        if not (a == 'X' or a == 'T'): xWon = False
        if not (a == 'O' or a == 'T'): oWon = False
    if xWon: return "X won"
    if oWon: return "O won"
    return False

def checkRow(rows, row):
    pos = []
    for j in range(len(rows)): pos.append([row, j])
    return check(rows, pos)

def checkCol(rows, col):
    pos = []
    for i in range(len(rows)): pos.append([i, col])
    return check(rows, pos)

def checkDiag1(rows):
    pos = []
    for i in range(len(rows)): pos.append([i, i])
    return check(rows, pos)

def checkDiag2(rows):
    pos = []
    for i in range(len(rows)): pos.append([i, len(rows)-i-1])
    return check(rows, pos)

def solveCase(rows):
    for i in range(len(rows)):
        result = checkRow(rows, i)
        if result: return result
    for j in range(len(rows)):
        result = checkCol(rows, j)
        if result: return result
    result = checkDiag1(rows) or checkDiag2(rows)
    if result: return result
    for i in range(len(rows)):
        for j in range(len(rows)):
            if rows[i][j] == ".": return "Game has not completed"
    return "Draw"

def process(data):
    out = ""
    caseNum = 1
    T = int(data[0])
    pos = 1
    for i in range(T):
        if caseNum > 1: out += '\n'
        n = 4
        lines = []
        for j in range(n): lines.append(data[pos+j])
        pos += (n + 1)
        out1 = "Case #" + str(caseNum) + ": "
        out1 += str(solveCase(lines))
        #print out1
        out += out1
        caseNum += 1
    return out

def main(fn):
    iFile = open(fn + ".in", "r")
    oFile = open(fn + ".out", "w")
    print("Files opened.")

    data = []
    while True:
        line = iFile.readline()
        if not line: break
        data.append(line)

    out = process(data)
    print("Calculations complete. Outputting to file.")
    oFile.writelines(out)
    print("Output complete.")
    iFile.close()
    oFile.close()
    print("Files closed.")

main("large")
