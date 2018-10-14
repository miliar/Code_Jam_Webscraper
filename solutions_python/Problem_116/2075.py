
def testLine(matrix, case):
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            if j == 0:
                symbol = matrix[i][j]
                if symbol == ".":
                    break
                elif symbol == "T":
                    symbol = matrix[i][j+1]
            if symbol != ".":
                if matrix[i][j] == symbol or matrix[i][j] == "T":
                    count += 1
                    if count == 4:
                        return "Case #{0}: {1} won".format(case + 1, symbol)
        count = 0
    return False

def testColumn(matrix, case):
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            if j == 0:
                symbol = matrix[j][i]
                if symbol == ".":
                    break
                elif symbol == "T":
                    symbol = matrix[j + 1][i]
            if symbol != ".":
                if matrix[j][i] == symbol or matrix[j][i] == "T":
                    count += 1
                    if count == 4:
                        return "Case #{0}: {1} won".format(case + 1, symbol)
        count = 0
    return False

def testDiagonalLR(matrix, case):
    count = 0
    symbol = matrix[0][0]
    if symbol == ".":
        return False
    elif symbol == "T":
        symbol = matrix[1][1]
    if symbol != ".":
        for i in range(0, 4):
            for j in range(0, 4):
                if i == j and (matrix[i][j] == symbol or matrix[i][j] == "T"):
                    count += 1
                    if count == 4:
                        return "Case #{0}: {1} won".format(case + 1, symbol)
        return False
    else:
        return False

def testDiagonalRL(matrix, case):
    count = 0
    symbol = matrix[0][3]
    if symbol == ".":
        return False
    elif symbol == "T":
        symbol = matrix[1][2]
    if symbol != ".":
        for i in range(0, 4):
            for j in range(0, 4):
                if i + j == 3 and (matrix[i][j] == symbol or matrix[i][j] == "T"):
                    count += 1
                    if count == 4:
                        return "Case #{0}: {1} won".format(case + 1, symbol)
        return False
    else:
        return False

def testDraw(matrix, case):
    for i in range(0,4):
        for j in range(0,4):
            if matrix[i][j] != ".":
                continue
            else:
                return False
    return "Case #{0}: Draw".format(case + 1)

if __name__ == "__main__":
    input = open("A-large.in")
    output = open("output.txt", "w")
    t = input.readline()
    source = []
    matrix = []
    for case in range(1, (int(t) * 5) + 1):
        line = input.readline()
        source += line.split()
        if case % 5 == 0:
            matrix.append(source)
            source = []
    for case in range(0, len(matrix)):
        if testLine(matrix[case], case) != False:
            output.write(testLine(matrix[case], case) + "\n")
        if testColumn(matrix[case], case) != False and not testLine(matrix[case], case):
           output.write(testColumn(matrix[case], case) + "\n")
        if testDiagonalRL(matrix[case], case) != False and not testLine(matrix[case], case) and not testColumn(matrix[case], case):
            output.write(testDiagonalRL(matrix[case], case) + "\n")
        if testDiagonalLR(matrix[case], case) != False and not testColumn(matrix[case], case) and not testLine(matrix[case], case) and not testDiagonalRL(matrix[case], case):
           output.write(testDiagonalLR(matrix[case], case) + "\n")
        if testDraw(matrix[case], case) != False and not testLine(matrix[case], case) and not testColumn(matrix[case], case) and not testDiagonalRL(matrix[case], case) and not testDiagonalLR(matrix[case], case):
           output.write(testDraw(matrix[case], case) + "\n")
        if not testLine(matrix[case], case) and not testColumn(matrix[case], case) and not testDiagonalRL(matrix[case], case) and not  testDiagonalLR(matrix[case], case) and not testDraw(matrix[case], case):
           output.write("Case #{0}: Game has not completed".format(case + 1) + "\n")

    output.close()
    input.close()


    
