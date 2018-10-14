def checkWin(matrix):
    sampleX = ["XXXX", "XXXT", "XXTX", "XTXX", "TXXX"]
    sample0 = ["OOOO", "OOOT", "OOTO", "OTOO", "TOOO"]

    #row
    for j in range(0, 4):
        if matrix[j] in sampleX:
            return "X won"
        if matrix[j] in sample0:
            return "O won"
    #column
    rwMatrix = ["", "", "", ""]
    for i in range(0, 4):
        for j in range(0, 4):
            rwMatrix[i] += "".join(matrix[j][i])
    for j in range(0, 4):
        if rwMatrix[j] in sampleX:
            return "X won"
        if rwMatrix[j] in sample0:
            return "O won"
    #diagonal
    diagonal1 = ""
    diagonal2 = ""
    for i in range(0, 4):
        diagonal1 += matrix[i][i]
        diagonal2 += matrix[3-i][i]
    if diagonal1 in sampleX or diagonal2 in sampleX:
        return "X won"
    if diagonal1 in sample0 or diagonal2 in sample0:
        return "O won"
    #contain .
    for i in range(0, 4):
        for j in range(0, 4):
            if matrix[i][j] == '.':
                return "Game has not completed"
    return "Draw"

def main():

    with open("A-large.in") as fi:
        T = int(fi.readline().strip())
        lines = {}
        for i in range(0,T):
            for j in range(0, 4):
                lines[j] = fi.readline().strip()
            #row
            fi.readline()
            print "Case #"+str(i+1)+": "+checkWin(lines)

if __name__ == '__main__':
    main()
