#!python3

inputFile = open("D-large.in", "r")
outputFile = open("output.txt", "w")

strShape = ["", "+", "x", "o"]

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):

    inp = inputFile.readline().split()
    n = int(inp[0]) + 1
    m = int(inp[1])

    mat = [[0 for x in range(n)] for y in range(n)]
    matp = [[0 for x in range(n)] for y in range(n)]
    matx = [[0 for x in range(n)] for y in range(n)]
    rmat = [[0 for x in range(n)] for y in range(n)]

    col = [0] * n
    row = [0] * n

    diagSum = [0] * (2 * n)
    diagDiff = [0] * (2 * n)

    for i in range(m):
        inp = inputFile.readline().split()
        tp = 0
        r = int(inp[1])
        c = int(inp[2])
        
        if inp[0] == "+":
            tp = 1
            matp[r][c] = 1
            diagSum[r + c] = 1
            diagDiff[r - c + n] = 1
        elif inp[0] == "x":
            tp = 2
            matx[r][c] = 2
            col[c] = 1
            row[r] = 1
        else:
            tp = 3
            matp[r][c] = 1
            matx[r][c] = 2
            diagSum[r + c] = 1
            diagDiff[r - c + n] = 1
            col[c] = 1
            row[r] = 1
        mat[r][c] = tp

    # Solving matx

    for r in range(1, n):
        if row[r] == 1:
            continue
        for c in range(1, n):
            if col[c] == 0:
                matx[r][c] = 2
                col[c] = 1
                row[r] = 1
                break

    # Solving matp

    for offset in range(0, n // 2):
        for c in range(1 + offset, n - offset):
            r = 1 + offset
            if diagSum[r + c] == 0 and diagDiff[r - c + n] == 0:
                matp[r][c] = 1
                diagSum[r + c] = 1
                diagDiff[r - c + n] = 1

        for r in range(1 + offset, n - offset):
            c = n - offset - 1
            if diagSum[r + c] == 0 and diagDiff[r - c + n] == 0:
                matp[r][c] = 1
                diagSum[r + c] = 1
                diagDiff[r - c + n] = 1

        for c in range(1 + offset, n - offset):
            r = n - offset - 1
            if diagSum[r + c] == 0 and diagDiff[r - c + n] == 0:
                matp[r][c] = 1
                diagSum[r + c] = 1
                diagDiff[r - c + n] = 1

        for r in range(1 + offset, n - offset):
            c = 1 + offset
            if diagSum[r + c] == 0 and diagDiff[r - c + n] == 0:
                matp[r][c] = 1
                diagSum[r + c] = 1
                diagDiff[r - c + n] = 1

    summ = 0
    strList = []

    for r in range(1, n):
        for c in range(1, n):
            rmat[r][c] = matp[r][c] + matx[r][c]

            if rmat[r][c] == 1 or rmat[r][c] == 2:
                summ += 1
            elif rmat[r][c] == 3:
                summ += 2

            if rmat[r][c] != mat[r][c]:
                strList.append(strShape[rmat[r][c]] + " " + str(r) + " " + str(c))
    
    print("Case #", testCase, ": ", summ, " ", len(strList), sep="", file=outputFile)

    for strL in strList:
        print(strL, file=outputFile)

inputFile.close()
outputFile.close()
