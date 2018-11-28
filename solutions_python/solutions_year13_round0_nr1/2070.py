SIZE = 4
PLAYER_A = "X"
PLAYER_B = "O"
JOKER = "T"
EMPTY = "."
INCOMPLETE = "Game has not completed"
LOSER = "LOSER"
players = [PLAYER_A, PLAYER_B]

def checkHorizontal(case):
    for line in case:
        winner = checkWinner(line)
        if winner != LOSER:
            return winner
    return LOSER

def checkVertical(case):
    return checkHorizontal(rotateList(case))

def checkDiagonalDown(case):
    line = case[0][0] + case[1][1] + case[2][2] + case[3][3]
    return checkWinner(line)

def checkDiagonalUp(case):
    line = case[0][3] + case[1][2] + case[2][1] + case[3][0]
    return checkWinner(line)

def checkWinner(line):
    winner = ""
    for player in players:
        count = line.count(player)
        if count == 4:
            winner = player
            return winner
        if count == 3:
            if line.count(JOKER) == 1:
                winner = player
                return winner
    return LOSER

def checkDrawAndIncompletion(case):
    completeLine = ""
    for line in case:
        completeLine = completeLine + line
    if completeLine.count(EMPTY) == 16 or completeLine.count(EMPTY) > 0:
        return INCOMPLETE
    else:
        return "Draw"

def rotateList(list):
    newList = []
    for i in range(SIZE):
        line = ""
        for j in range(SIZE):
            line = line + list[j][i]
        newList.append(line)
    return newList
        
def main():
    inFile = open("A-large.in", "r")
    outFile = open("problem.out", "w")
    
    lines = inFile.read().split()
    inFile.close()
    
    numberOfCases = int(lines[0])
    lines.pop(0)
    
    for i in range(0, numberOfCases):
        case = lines[(i * SIZE):((i + 1) * SIZE)]
        
        result = LOSER
        result = checkHorizontal(case)
        if result == LOSER:
            result = checkVertical(case)
            if result == LOSER:
                result = checkDiagonalDown(case)
                if result == LOSER:
                    result = checkDiagonalUp(case)
                    if result == LOSER:
                        result = checkDrawAndIncompletion(case)
        
        if result == PLAYER_A or result == PLAYER_B:
            result = result + " won"
        result = "Case #" + str(i + 1) + ": " + result + "\n"
        print(result)
        outFile.write(result);
    
    outFile.close()

main()