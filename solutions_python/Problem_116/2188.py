def check_rows(b):
    result = None
    for i in xrange(4):
        sorted_row = sorted(b[i])
        if sorted_row == ['T', 'X', 'X', 'X'] or sorted_row == ['X', 'X', 'X', 'X']:
            result = "X won"
        elif sorted_row == ['O', 'O', 'O', 'T'] or sorted_row == ['O', 'O', 'O', 'O']:
            result = "O won"

    return result

def check_columns(b):
    result = None
    for i in xrange(4):
        sorted_column = sorted([b[0][i], b[1][i], b[2][i], b[3][i]])
        if sorted_column == ['T', 'X', 'X', 'X'] or sorted_column == ['X', 'X', 'X', 'X']:
            result = "X won"
        elif sorted_column == ['O', 'O', 'O', 'T'] or sorted_column == ['O', 'O', 'O', 'O']:
            result = "O won"

    return result
 

def check_diagonals(b):
    result = None
    d1 = sorted([b[0][0], b[1][1], b[2][2], b[3][3]])
    d2 = sorted([b[0][3], b[1][2], b[2][1], b[3][0]])

    if d1 == ['T', 'X', 'X', 'X'] or d1 == ['X', 'X', 'X', 'X']:
        result = "X won"
    elif d2 == ['T', 'X', 'X', 'X'] or d2 == ['X', 'X', 'X', 'X']:
        result = "X won"
    elif d1 == ['O', 'O', 'O', 'T'] or d1 == ['O', 'O', 'O', 'O']:
        result = "O won"
    elif d2 == ['O', 'O', 'O', 'T'] or d2 == ['O', 'O', 'O', 'O']:
        result = "O won"

    return result

def determine_tie(b):
    result = "Draw"
    for i in xrange(4):
        for j in xrange(4):
            if b[i][j] == ".":
                result = "Game has not completed"

    return result

def main():
    f = open("A-large.in")
    cases = int(f.readline())

    for i in xrange(cases):
        board = []
        
        for j in xrange(4):
            line = f.readline().strip("\n")
            board.append(list(line))

        result = check_rows(board)

        if result == None:
            result = check_columns(board)

        if result == None:
            result = check_diagonals(board)

        if result == None:
            result = determine_tie(board)

        print "Case #" + str(i+1) + ": " + result

        # Skip blank line
        f.readline()

if __name__ == '__main__':
    main()
