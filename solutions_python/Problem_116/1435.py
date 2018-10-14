

with open("A-large.in", "rb") as f:
    lines = f.readlines()


nb = int(lines[0])


def checkwinner(row):
    if all(x == "X" or x == "T" for x in row):
        return "X"
    if all(x == "O" or x == "T" for x in row):
        return "O"
    return None

def analyze(testcase):
    tocheck = []
    #rows
    for i in range(4):
        tocheck.append(testcase[i])
    #cols
    for i in range(4):
        tocheck.append(zip(*testcase)[i])
    #diags
    tocheck.append([testcase[i][i] for i in range(4)])
    tocheck.append([testcase[3-i][i] for i in range(4)])
    winners = [checkwinner(c) for c in tocheck]
    for w in winners:
        if w == "X":
            return "X won"
        if w == "O":
            return "O won"
    for i in range(4):
        for j in range(4):
            if testcase[i][j] == ".":
                return "Game has not completed"
    return "Draw"

with open("outf_large.txt", "wb") as fout:
             
    for n in range(nb):
        testcase = [[None] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                testcase[i][j] = lines[n * 5 + 1 + i][j]
        fout.write("Case #%d: %s\n" % (n+1, analyze(testcase)))

