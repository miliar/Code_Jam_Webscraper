def product(x):
    sum = x[0]
    for i in range(1, len(x)):
        sum *= x[i]
    return sum

VALUES_MAP = {'.': 0, 'T':1, 'X': 2, 'O': 3}

cases = int(raw_input())

for case in range(cases):
    board = []
    for row in range(4):
        board.append([VALUES_MAP[v] for v in raw_input()])

    raw_input() # ignore blank line

    rows = [product(x) for x in board]
    cols = [product(x) for x in zip(*board)]
    diags = [product([board[i][i] for i in range(4)]),
            product([board[i][3-i] for i in range(4)])]

    print "Case #" + str(case + 1) + ":",
    seenEmpty = False
    foundWinner = False

    for i in rows + cols + diags:
        if i == 8 or i == 16:
            foundWinner = True
            print "X won"
            break
        elif i == 27 or i == 81:
            foundWinner = True
            print "O won"
            break
        elif i == 0:
            seenEmpty = True

    if not foundWinner:
        if seenEmpty:
            print "Game has not completed"
        else:
            print "Draw"
