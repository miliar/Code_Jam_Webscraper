def valid(desired, height, heightLocations):
    rowsOccupied = set()
    columnsOccupied = set()
    for position in heightLocations[height]:
        rowsOccupied.add(position[0])
        columnsOccupied.add(position[1])
    for row in rowsOccupied:
        for column in columnsOccupied:
            if desired[row][column] < height:
                return False
    return True

inputFile = open("QualificationBsmall.in", "r")
outputFile = open("QualificationBsmall.txt", "w")

cases = int(inputFile.readline().strip())
for caseIndex in range(1, cases + 1):
    height, width = map(int, inputFile.readline().strip().split(" "))
    desired = []
    for i in range(height):
        desired.append(map(int,filter(None, inputFile.readline().strip().split(" "))))
    heightLocations = {} #height:[list of height locations in form(row, col)]

    # get locations of cells with a given height
    for row in range(height):
        for column in range(width):
            cell = desired[row][column]
            if cell in heightLocations:
                heightLocations[cell].append((row, column))
            else:
                heightLocations[cell] = [(row, column)]

    #validify
    if all([valid(desired, height, heightLocations) for height in heightLocations]):
        result = "YES"
    else:
        result = "NO"

    outputFile.write("Case #%d: %s\n" % (caseIndex, result))


inputFile.close()
outputFile.close()