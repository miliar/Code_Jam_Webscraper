

inFile = open("A-small-attempt0.in", "r")
outFile = open("output.txt", "w")

numTests = int(inFile.readline())

for j in range(numTests):
    ans = inFile.readline()

    row1A = (inFile.readline().rstrip()).split(" ")
    row2A = (inFile.readline().rstrip()).split(" ")
    row3A = (inFile.readline().rstrip()).split(" ")
    row4A = (inFile.readline().rstrip()).split(" ")
    rows = [row1A, row2A, row3A, row4A]

    relevantRow1 = rows[int(ans) - 1]

    ans2 = inFile.readline()

    row1B = (inFile.readline().rstrip()).split(" ")
    row2B = (inFile.readline().rstrip()).split(" ")
    row3B = (inFile.readline().rstrip()).split(" ")
    row4B = (inFile.readline().rstrip()).split(" ")

    rowsB = [row1B, row2B, row3B, row4B]

    relevantRow2 = rowsB[int(ans2) - 1]

    possibleSolutions = []
    for i in relevantRow1:
        if i in relevantRow2:
            possibleSolutions.append(i)

    result = ""
    if len(possibleSolutions) > 1:
        result = "Bad magician!"
    elif len(possibleSolutions) == 0:
        result = "Volunteer cheated!"
    else:
        result = str(possibleSolutions[0])
    outFile.write("Case #{}: {}\n".format(j+1, result))

outFile.close()
inFile.close()