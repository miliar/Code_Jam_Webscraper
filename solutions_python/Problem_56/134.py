import sys

def print_board(board, N) :
    # Write board
    print
    for jj in xrange(0, N, 1):
        for kk in xrange(0, N, 1):
            print board[jj][kk],
        print

def rotate_board(board, N) :
    new_board = []
    for ii in xrange(0, N, 1) :
        row = []
        for jj in xrange(N - 1, -1, -1) :
            row.append(board[jj][ii])
        new_board.append(row)
    return new_board

def apply_gravity(board, N):
    new_board = []
    for ii in xrange(0, N, 1) :
        row = []
        new_board.append(row)

    for ii in xrange(0, N, 1) :
        column = []
        for jj in xrange(N - 1, -1, -1) :
            if (board[jj][ii] == ".") :
                continue
            else :
                column.append(board[jj][ii])
        for jj in xrange(len(column), N, 1) :
            column.append(".")
        #print column
        for kk in xrange(N-1, -1, -1) :
            new_board[kk].append(column.pop(0))

    return new_board

def check_winner(board, player, K, N):
    winning_str = ""
    for ii in xrange(0, K, 1) :
        winning_str += player
    #print winning_str
    # Check rows
    for ii in xrange(0, N, 1) :
        str = ""
        for jj in xrange(0, N, 1) :
            str += board[ii][jj]
        #print str
        if (str.find(winning_str) != -1) :
            return True
    # Check Columns
    for ii in xrange(0, N, 1) :
        str = ""
        for jj in xrange(0, N, 1) :
            str += board[jj][ii]
        #print str
        if (str.find(winning_str) != -1) :
            return True
    # Check Diagonals
    x = 0
    y = 0

    # Diagonals Upper Right to Lower Left
    for ii in xrange(0, N, 1) :
        saved_x = x
        str = ""
        while (x > -1) :
            str += board[x][y]
            x -= 1
            y += 1
        if (str.find(winning_str) != -1) :
            return True
        x = saved_x + 1
        y = 0

    y = 1
    for ii in xrange(0, N - 1, 1) :
        saved_y = y
        x = N - 1
        str = ""
        while (y < N) :
            str += board[x][y]
            x -= 1
            y += 1
        if (str.find(winning_str) != -1) :
            return True
        y = saved_y + 1

    # Diagonals Upper Left to Lower Right
    x = N - 1
    y = 0
    for ii in xrange(0, N, 1) :
        saved_x = x
        str = ""
        while (x < N) :
            str += board[x][y]
            x += 1
            y += 1
        if (str.find(winning_str) != -1) :
            return True
        x = saved_x - 1
        y = 0
    y = 1
    for ii in xrange(0, N - 1, 1) :
        saved_y = y
        x = 0
        str = ""
        while (y < N) :
            #print x, y
            str += board[x][y]
            x += 1
            y += 1
        if (str.find(winning_str) != -1) :
            return True
        y = saved_y + 1


    return False

def main() :
    if (len(sys.argv) != 2) :
        print sys.argv[0] + " [input file]"
        return

    input = open(sys.argv[1])

    limit = int(input.readline())
    print "Handling " + str(limit) + " cases."

    output = open("output.txt", "w")

    for ii in xrange(0, limit, 1) :
        line = input.readline()
        # strip new line
        line = line[:-1]
        line = line.split()
        N = int(line[0])
        K = int(line[1])
        board = []
        for jj in xrange(0, N, 1) :
            line = input.readline()
            line = line[:-1]
            row = []
            for kk in xrange(0, N, 1) :
                row.append(line[kk])
            board.append(row)
        #print_board(board, N)
        board = rotate_board(board, N)
        #print_board(board, N)
        board = apply_gravity(board, N)
        #print_board(board, N)
        winnerR = check_winner(board, "R", K, N)
        winnerB = check_winner(board, "B", K, N)
        string = "Neither"
        if (winnerR and winnerB) :
            string = "Both"
        elif (winnerR and not winnerB) :
            string = "Red"
        elif (winnerB and not winnerR) :
            string = "Blue"
        output.write("Case #" + str(ii+1) + ": " + string + "\n")

    input.close()
    output.close()

if __name__ == "__main__" :
    main()
