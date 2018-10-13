def solveCase(case):
    gameOver = True
    totalWinner = 'T'

    # horisontal
    for i in range(0, 4):
        winner = 'T'
        
        for j in range(0, 4):
            newWinner = case[i][j]
            if newWinner == '.':
                gameOver = False
                winner = 'T'
                break

            if newWinner == 'T':
                continue

            if winner != 'T':
                if newWinner != winner:
                    winner = 'T'
                    break
            winner = newWinner

        if winner != 'T':
            totalWinner = winner
            break

    # vertical
    for j in range(0, 4):
        winner = 'T'
        
        for i in range(0, 4):
            newWinner = case[i][j]
            if newWinner == '.':
                gameOver = False
                winner = 'T'
                break

            if newWinner == 'T':
                continue

            if winner != 'T':
                if newWinner != winner:
                    winner = 'T'
                    break
            winner = newWinner

        if winner != 'T':
            totalWinner = winner
            break

    #diagonal 1
    winner = 'T'
    
    for i in range(0, 4):
        newWinner = case[i][i]
        if newWinner == '.':
            gameOver = False
            winner = 'T'
            break

        if newWinner == 'T':
            continue

        if winner != 'T':
            if newWinner != winner:
                winner = 'T'
                break
        winner = newWinner

    if winner != 'T':
        totalWinner = winner

    #diagonal 2
    winner = 'T'
    
    for i in range(0, 4):
        newWinner = case[i][3 - i]
        if newWinner == '.':
            gameOver = False
            winner = 'T'
            break

        if newWinner == 'T':
            continue

        if winner != 'T':
            if newWinner != winner:
                winner = 'T'
                break
        winner = newWinner

    if winner != 'T':
        totalWinner = winner

    print(case)
    print(gameOver, totalWinner)

    results = ["X won",
               "O won",
               "Draw",
               "Game has not completed"]
    
    if totalWinner == 'T':
        if gameOver:
            return results[2]
        else:
            return results[3]
    else:
        if totalWinner == 'X':
            return results[0]
        else:
            return results[1]      
    

def solve(sourceFile, resultFile):
    s = open(sourceFile)
    r = open(resultFile, 'w')

    count = int(s.readline())
    for n in range(1, count + 1):
        case = []
        for i in range(0, 4):
            line = s.readline().strip()
            case.append(line)
        s.readline()

        header = 'Case #' + str(n) + ': '
        r.write(header + solveCase(case) + '\n')
    return
        
def main():
    source = 'A-small-attempt0 (1).in'
    result = source + '.result.txt'
    solve(source, result)
    return

if __name__ == '__main__':
    main()
