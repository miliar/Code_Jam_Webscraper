T = int(raw_input(''))
for t in range(T):
    board = [raw_input(''),raw_input(''),raw_input(''),raw_input('')]
    raw_input('')
    result = None
    # Check for 4 of something in a row
    for row in board:
        if result != None:
            break
        if all(map(lambda x: x == 'X' or x == 'T',row)):
            result = "X won"
        if all(map(lambda x: x == 'O' or x == 'T',row)):
            result = "O won"
    
    for idx in range(4):
        if result != None:
            break
        col = map(lambda r: r[idx],board)
        if all(map(lambda x: x == 'X' or x == 'T',col)):
            result = "X won"
        if all(map(lambda x: x == 'O' or x == 'T',col)):
            result = "O won"

    ldiag = []
    rdiag = []
    for idx in range(4):
        ldiag.append(board[idx][idx])
        rdiag.append(board[idx][3-idx])

    if any(map(lambda r: all(map(lambda x: x == 'X' or x == 'T',r)), [ldiag,rdiag])):
        result = "X won"
    if any(map(lambda r: all(map(lambda x: x == 'O' or x == 'T',r)), [ldiag,rdiag])):
        result = "O won"

    if result == None:
        if any(map(lambda row: any(map(lambda c: c == '.',row)) ,board)):
            result = "Game has not completed"
        else:
            result = "Draw"

    print ("Case #%d:"%(t+1)), result#, debuglevels
