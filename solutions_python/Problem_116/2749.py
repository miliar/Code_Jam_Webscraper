X = "X"
T = "T"
O = "O"
D = "."

def are_equal(f1, f2):
    if f1 == T and f2 == T:
        return T
    if f1 == T:
        if f2 == X or f2 == O:
            return f2
        else:
            return None
    elif f2 == T:
        if f1 == X or f1 == O:
            return f1
        else:
            return None    
    else:
        if "." in [f1,f2]:
            return None
        else:
            if f1 == f2:
                return f1
            else:
                return None

assert are_equal("X", "T")
assert are_equal("O", "T")
assert are_equal("T", "X")
assert are_equal("T", "O")
assert not are_equal("X", "O")
assert not are_equal("O", "X")
assert not are_equal("X", ".")
assert not are_equal("T", ".")
assert not are_equal(".", "X")
assert not are_equal(".", "T")

def is_won_row(row):
    assert len(row) == 4
    correct = 0
    is_correct = True
    prev = None
    won = None
    
    for i in row:
        if not prev:
            prev = i
            continue
        else:
            t = are_equal(prev, i)
            if t:
                tmp = True
                if t != T:
                    won = t
            else:
                tmp = False
            is_correct = is_correct and tmp
            if is_correct:
                correct += 1
            prev = i
    
    if correct == 3 and is_correct:
        return won
    else:
        return None

assert not is_won_row("....")
assert is_won_row("XXXT")
assert is_won_row("TXXX")
assert is_won_row("TOOO")
assert is_won_row("OOOT")

def is_won_col(board):
    assert len(board) == 4
    
    col1 = ""
    col2 = ""
    col3 = ""
    col4 = ""

    for n in board:
        assert len(n) == 4
        col1 += n[0]
        col2 += n[1]
        col3 += n[2]
        col4 += n[3]

    return is_won_row(col1) or is_won_row(col2) or is_won_row(col3) or is_won_row(col4)

def is_won_diag(board):
    assert len(board) == 4
    
    diag_i = []
    diag_j = []
    i = 0
    j = 3

    for n in board:
        assert len(n) == 4
        diag_i.append(n[i])
        diag_j.append(n[j])
        i += 1
        j -= 1

    return is_won_row(''.join(diag_i)) or is_won_row(''.join(diag_j))

assert is_won_diag(["OXXX", "XO..", "..O.","...O"])
assert is_won_diag(["...O", "..O.", "XO..", "OXXX"])
assert is_won_diag(["XXXO", "..O.", ".O..", "T..."])

def get_boards(path):
    boards = []
    f = open(path, 'r')
    lines = f.readlines()

    board = []
    for line in lines:
        if len(line) > 3:
            board.append(line.strip())
        else:
            if len(board) > 0:
                boards.append(board)
            board = []

    return boards

def is_won_by_row(board):
    for row in board:
        v = is_won_row(row)
        if v:
            return v
    return None

def is_filled(board):
    for row in board:
        if D in row:
            return False
    return True

def output(path):
    boards = get_boards(path)
    p_out = "Case #%d: %s"

    i = 1
    for board in boards:
        #print i, board
        won = False
        v = is_won_by_row(board)
        if v:
            print p_out % (i, "%s won" % v)
            won = True
        
        v = is_won_col(board)
        if not won and v:
            print p_out % (i, "%s won" % v)
            won = True
        
        v = is_won_diag(board)
        if not won and v:
            print p_out % (i, "%s won" % v)
            won = True        

        if not won:
            if is_filled(board):
                print p_out % (i, "Draw")
            else:
                print p_out % (i, "Game has not completed")
        i += 1

output("A-small-attempt1.in")



