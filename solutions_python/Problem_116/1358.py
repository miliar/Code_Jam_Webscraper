cases = int(raw_input())

def readboard():
    b = [raw_input(), raw_input(), raw_input(), raw_input()]
    try:
        raw_input()
    except:
        pass
    return b

def cell_matches(player, value):
    assert player in 'XO'
    return value == player or value == 'T'

def check_row(i, b):
    for player in 'XO':
        if all(cell_matches(player, b[i][j]) for j in range(4)):
            return player
    return None

def check_col(i, b):
    for player in 'XO':
        if all(cell_matches(player, b[j][i]) for j in range(4)):
            return player
    return None

def check_diag(b):
    for player in 'XO':
        if all(cell_matches(player, b[j][j]) for j in range(4)):
            return player

        if all(cell_matches(player, b[j][3-j]) for j in range(4)):
            return player

    return None
    

def check_board(b):
    # for r in
    #     if '.' in r:
    #         return 'Game has not completed'

    
    for i in range(4):
        winner = check_row(i, b)
        if winner is not None:
            return "{} won". format(winner)

        winner = check_col(i, b)
        if winner is not None:
            return "{} won". format(winner)

    winner = check_diag(b)

    if winner is not None:
        return "{} won". format(winner)
    else:
        for r in board:
            if '.' in r:
                return 'Game has not completed'
        return "Draw"





for x in range(cases):
    board = readboard()
    # print board
    result = check_board(board)
    print "Case #{}: {}".format(x+1, result)
