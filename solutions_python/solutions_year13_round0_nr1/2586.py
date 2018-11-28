def process_file(f):
    ''' This function processes the given file. '''

    fIn = open(f, "r")

    fLine = fIn.readline()
    numCases = int(fLine.strip())
    caseDict = {}
    counter = 1
    
    fLine = fIn.readline()
    while counter <= numCases and fLine:
        mainL = []
        while fLine and fLine.strip() != "":
            subL = []
            for c in fLine.strip():
                subL.append(c)
            mainL.append(subL)
            fLine = fIn.readline()

        caseDict[counter] = mainL
        fLine = fIn.readline()
        counter += 1
    
    return caseDict

def process_cases(cases):
    ''' This function goes through all the game cases. 
        Once the results are received it is written into a text file.'''

    fOut = open('output.txt', 'w')

    for key in range(1, len(cases.keys()) + 1):
        res = process_case(cases[key])
        if res == 0:
            fOut.write("Case #" + str(key) + ": " + "Game has not completed\n")
            print "Case #" + str(key) + ": " + "Game has not completed"
        elif res == "Draw":
            fOut.write("Case #" + str(key) + ": " + res + "\n")
            print "Case #" + str(key) + ": " + res
        else:
            fOut.write("Case #" + str(key) + ": " + res + " won\n")
            print "Case #" + str(key) + ": " + res + " won"


def process_case(case):
    ''' This function goes through every element in the game board. '''

    period_counter = 0
    for x in range(len(case)):
        for y in range(len(case)):
            res = 0

            if case[x][y] == ".":
                period_counter += 1
            elif case[x][y] != "T":
                if x == 0 and (y == 0 or y == len(case) - 1):
                    res = checkDiag(case, case[x][y], x, y, "none")
                    if res != 0:
                        return res
                res = checkVertical(case, case[x][y], x, y, "none")
                if res != 0:
                    return res

                res = checkHorizontal(case, case[x][y], x, y, "none")
                if res != 0:
                    return res

    # Check if its a draw or game not completed.
    if period_counter == 0:
        return "Draw"
    return 0


def checkDiag(case, valS, x, y, direction):
    ''' This function checks if there are and diagonals matching. '''

    if case[x][y] != "T" and case[x][y] != valS:
        return 0

    if (direction == "none" and y == 0) or direction == "right":
        if x == len(case) - 1 and y == len(case) - 1:
            return valS
        return checkDiag(case, valS, x + 1, y + 1, "right")
    elif (direction == "none" and y == len(case) - 1) or direction == "left":
        if x == len(case) - 1 and y == 0:
            return valS
        return checkDiag(case, valS, x + 1, y - 1, "left")

def checkVertical(case, valS, x, y, direction):
    ''' This function checks if there are any matching vertical. '''

    if x >= len(case) or x < 0:
        return valS
    elif case[x][y] != "T" and case[x][y] != valS:
        return 0

    if direction == "up":
        return checkVertical(case, valS, x - 1, y, "up")
    if direction == "down":
        return checkVertical(case, valS, x + 1, y, "down")
    
    if direction == "none":
        resUp = checkVertical(case, valS, x - 1, y, "up")
        resDown = checkVertical(case, valS, x + 1, y, "down")

        if resUp == resDown:
            return resUp
        else:
            return 0

def checkHorizontal(case, valS, x, y, direction):
    ''' This function checks if there are any matching horiontal. '''

    if y >= len(case) or y < 0:
        return valS
    elif case[x][y] != "T" and case[x][y] != valS:
        return 0

    if direction == "right":
        return checkHorizontal(case, valS, x, y + 1, "right")
    if direction == "left":
        return checkHorizontal(case, valS, x, y - 1, "left")

    if direction == "none":
        resRight = checkHorizontal(case, valS, x, y + 1, "right")
        resLeft = checkHorizontal(case, valS, x, y - 1, "left")

        if resRight == resLeft:
            return resRight
        else: 
            return 0

if __name__ == "__main__":
    case = process_file("A-small-attempt0.in")
    process_cases(case)