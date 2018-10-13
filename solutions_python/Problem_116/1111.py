def solutions(board):
    l = []

    for i in range(len(board)):
        l.append(board[i])
        l.append([board[0][i], board[1][i], board[2][i], board[3][i]])

    l.append([board[0][0], board[1][1], board[2][2], board[3][3]])
    l.append([board[0][3], board[1][2], board[2][1], board[3][0]])

    return l
 
def checkSolution(solution):
    for n, i in enumerate(solution):
        if i is 'T':
            if n is 0:
                solution[n] = solution[1]
            else:
                solution[n] = solution[0]
        if i is '.':
            return False

    return solution[0] == solution[1] == solution[2] == solution[3]
 
def checkAllSolutions(solutions):
    winner = False
    draw = True
    player = ''
    for solution in solutions:
        if '.' in solution:
            draw = False
        if checkSolution(solution):
            winner = True
            player = solution[0]
    return winner, draw, player
 
if __name__ == "__main__":
    problems = None;
    case = 1

    with open('input.txt', 'r') as f:
        content = f.readlines()
        content.pop(0)
        problems = content

    problems = [p.rstrip() for p in problems]
    problems = [list(p) for p in problems]
    problems = filter(None, problems)
    problems = [problems[n:n + 4] for n in range(0, len(problems), 4)]

    for problem in problems:
        winner, draw, player = checkAllSolutions(solutions(problem))
        if winner:
            print "Case #%d: %s won" % (case, player)
        elif draw:
            print "Case #%d: Draw" % (case)
        else:
            print "Case #%d: Game has not completed" % (case)

        case += 1