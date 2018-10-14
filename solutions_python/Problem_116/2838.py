import time

def check(game_board):
    diagonal_right = ""
    diagonal_left = ""
    diagonal_board = []
    verticle_board = []
    y = 0
    for row in xrange(4):
        if game_board[row].count("XXXT") > 0 or game_board[row].count("XXXX") > 0:
            return "X won"
        elif game_board[row].count("OOOT") > 0 or game_board[row].count("OOOO") > 0:
            return "O won"

    for column in xrange(4):
        verticle_board = zip(*game_board)
        if verticle_board[column].count("X") > 3 or (verticle_board[column].count("X") > 2 and verticle_board[column].count("T") > 0):
            return "X won"
        elif verticle_board[column].count("O") > 3 or (verticle_board[column].count("O") > 2 and verticle_board[column].count("T") > 0):
            return "O won"

    for x in xrange(4):
        diagonal_right += game_board[x][x]
    for x in xrange(4):
        y = 3-x
        diagonal_left += game_board[x][y]
    diagonal_board.append(diagonal_left)
    diagonal_board.append(diagonal_right)
    for line in diagonal_board:
        if line.count("XXXT") > 0 or line.count("XXXX") > 0:
            return "X won"
        elif line.count("OOOT") > 0 or line.count("OOOO") > 0:
            return "O won"

    for row in xrange(4):
        if game_board[row].count(".") > 0:
            return "Game has not completed"
    return "Draw"

def main():
    time_start = time.clock()
    test = open('A-small-attempt0.in','r')
    test_number = int(test.readline())

    for x in xrange(1, test_number+1):

        game_board = []
        for row in xrange(4):
            game_board.append(test.readline())
        test.readline()
        result = check(game_board)

        print "Case #" + str(x) + ": " + result

    test.close()
    print "Time used: " + str(time.clock() - time_start) + " seconds"

if __name__ == '__main__':
    main()
