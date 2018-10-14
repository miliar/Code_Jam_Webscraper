def checkCondition(board):
    players = ["X", "O"]

    for player in players:
        for pivot in xrange(4):
            # vertical check
            if all(token in [player, "T"] for token in [board[y][pivot] for y in xrange(4)]):
                return player + " won"
            # horizontal check
            if all(token in [player, "T"] for token in [board[pivot][x] for x in xrange(4)]):
                return player + " won"
        # diagonals check
        if all(token in [player, "T"] for token in [board[x][x] for x in xrange(4)]):
            return player + " won"
        if all(token in [player, "T"] for token in [board[3-x][x] for x in xrange(4)]):
            return player + " won"

    # check for game in progress (dot)
    for i in xrange(4):
        if board[i].find(".") != -1:
            return "Game has not completed"
        
    return "Draw"
    

fin = open("A-large.in")
fout = open("prob1.out", "w")

num_cases = int(fin.readline())

for case_number in xrange(num_cases):
    board = []
    board.append(fin.readline())
    board.append(fin.readline())
    board.append(fin.readline())
    board.append(fin.readline())
    result = checkCondition(board)
    print result
    fout.write("Case #%d: %s\n" % (case_number+1, result))
    fin.readline()
    

fout.close()
