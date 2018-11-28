numCases = int(input())
for i in range(1, numCases+1):
    numRows, numCols = [int(s) for s in raw_input().split(" ")]
    rows = []

    for currRow in xrange(numRows):
        rows.append(list(raw_input()))
        fillNum = 0
        fillChar = ''
        newRow = []
        for index in xrange(numCols):
            if(rows[currRow][index] == '?'):
                fillNum += 1

            if(rows[currRow][index] != '?'):
                    fillChar = rows[currRow][index]
                    newRow += [fillChar]

            if((rows[currRow][index] != '?' or (index + 1) == numCols) and fillNum > 0):
                tempRow = [fillChar] * fillNum
                newRow += tempRow
                fillNum = 0
        rows[currRow] = newRow

    rowsToFill = 0
    fillIndex = 0
    for currRow in xrange(numRows):
        if (rows[currRow][0] == ""):
            rowsToFill += 1
        else:
            fillIndex = currRow

        if((rows[currRow][0] != '' or (currRow + 1) == numRows) and rowsToFill > 0):
            for index in range(currRow-rowsToFill, currRow+1):
                rows[index] = rows[fillIndex]
            rowsToFill = 0

    print("Case #{}:").format(i)
    for currRow in xrange(numRows):
        print(''.join(str(v) for v in rows[currRow]))
