#!python3

inputFile = open("A-large.in", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):

    inp = inputFile.readline().split()
    r = int(inp[0])
    c = int(inp[1])

    cake = []

    for i in range(r):
        cake.append(list(inputFile.readline().strip()))

    # Go Down and Up

    for row in range(r):
        for col in range(c):
            if cake[row][col] != '?':
                for row1 in range(row - 1, -1, -1):
                    if cake[row1][col] == '?':
                        cake[row1][col] = cake[row][col]
                    else:
                        break
                for row2 in range(row + 1, r):
                    if cake[row2][col] == '?':
                        cake[row2][col] = cake[row][col]
                    else:
                        break

    for col in range(c):
        for row in range(r):
            if cake[row][col] != '?':
                for col1 in range(col - 1, -1, -1):
                    if cake[row][col1] == '?':
                        cake[row][col1] = cake[row][col]
                    else:
                        break
                for col2 in range(col + 1, c):
                    if cake[row][col2] == '?':
                        cake[row][col2] = cake[row][col]
                    else:
                        break

    

    print("Case #", testCase, ":", sep="", file=outputFile)

    for row in cake:
        print("".join(row), file=outputFile)

inputFile.close()
outputFile.close()
