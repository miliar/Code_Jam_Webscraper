import sys

def main():
    filename = sys.argv[1]
    inputFile = open(filename+".in").read();
    outputFile = open(filename+ ".out", "w")
    lines = inputFile.splitlines()
    lines.reverse()
    testCases = lines.pop()

    for test in range(0, int(testCases)):
        nm = lines.pop().split(" ")
        N = int(nm[0])
        M = int(nm[1])
        lawn = []
        for row in range (0, N):
            lawn.append(list(lines.pop().split(" ")))
        result = "YES" if checkLawn(lawn, N, M) else "NO"
        outputFile.write("Case #" + str(test+1) + ": " + result + "\n")

def checkLawn(lawn, N, M):
    rowMin = [100]*N
    colMin = [100]*M

    for row in range(0, N):
        for col in range(0, M):
            rowValid = validStrip(lawn[row], lawn[row][col])
            if (not rowValid):
                colStrip = column(lawn, col)
                colValid = validStrip(colStrip, lawn[row][col])
                if(not colValid):
                    return False

    return True

def validStrip(strip, checkHeight):
    for cell in range(0, len(strip)):
        if (strip[cell] > checkHeight):
            return False

    return True


def column(matrix, i):
    return [row[i] for row in matrix]

main()